_PROFILE = True

import time
import weakref

if _PROFILE:
    import cProfile
    import pstats
    import io


class profile_deco:
    def __init__(self, func):
        self._func = func
        self._profile = cProfile.Profile() if _PROFILE else None

    def __call__(self, *args, **kwargs):
        if self._profile is not None:
            self._profile.enable()

        result = self._func(*args, **kwargs)

        if self._profile is not None:
            self._profile.disable()

        return result

    def print_stat(self):
        if self._profile is not None:
            s = io.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(self._profile, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())


class Attr:
    pass


class ObjectWithAttr:
    def __init__(self, attr):
        self.attr = attr


class ObjectWithSlot:
    __slots__ = ('attr',)

    def __init__(self, attr):
        self.attr = attr


class ObjectWithWeakref:
    def __init__(self, attr):
        self.attr = weakref.ref(attr)


@profile_deco
def bulk_create(points, attr, point_class):
    for i in range(len(points)):
        points[i] = point_class(attr)


@profile_deco
def bulk_read(points, attr):
    dummy = None
    for i in range(len(points)):
        dummy = points[i].attr


@profile_deco
def bulk_update(points, attr):
    for i in range(len(points)):
        points[i].attr = attr


@profile_deco
def bulk_delete(points, attr):
    for i in range(len(points)):
        del points[i].attr


def measure_run_time(func, *args):
    start = time.monotonic()
    func(*args)
    end = time.monotonic()
    return '{:.3f}'.format(end - start)


def main(bulk_size=1000000):
    attr = Attr()
    points = [None] * bulk_size

    for point_class in (ObjectWithAttr, ObjectWithSlot, ObjectWithWeakref):
        print(point_class.__name__, measure_run_time(bulk_create, points, attr, point_class), end='')
        for method in (bulk_read, bulk_update, bulk_delete):
            print(' ' + measure_run_time(method, points, attr), end='')
        print()

    if not _PROFILE:
        return

    for method in (bulk_create, bulk_read, bulk_update, bulk_delete):
        print()
        method.print_stat()


if __name__ == '__main__':
    main()
