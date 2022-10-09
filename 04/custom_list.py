import itertools
import functools
import operator


class CustomList(list):
    def __str__(self):
        return super().__str__() + ' sum: ' + str(sum(self))

    def __sub__(self, other):
        return self.__apply_op(self, other, operator.sub)

    def __rsub__(self, other):
        return self.__apply_op(other, self, operator.sub)

    def __add__(self, other):
        return self.__apply_op(self, other, operator.add)

    def __radd__(self, other):
        return self.__apply_op(other, self, operator.add)

    @staticmethod
    def __apply_op(left, right, op):
        return CustomList(
            itertools.starmap(
                op,
                itertools.zip_longest(left, right, fillvalue=0)
            )
        )


def __override_comparison_methods():
    def compare(self, other, op):
        return op(sum(self), sum(other))

    for name in ('lt', 'le', 'eq', 'ne', 'gt', 'ge'):
        setattr(
            CustomList,
            f'__{name}__',
            functools.partialmethod(
                compare,
                op=getattr(operator, f'__{name}__')
            )
        )


__override_comparison_methods()
