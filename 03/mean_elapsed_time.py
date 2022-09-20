import dataclasses
import time
import queue


def mean(wndsize):
    @dataclasses.dataclass
    class CallTimeStats:
        lastRuns: queue.Queue = None
        timeAccum: float = 0

        def updateTime(self, elapsedTime) -> None:
            if self.lastRuns is None:
                self.lastRuns = queue.Queue()

            self.lastRuns.put(elapsedTime)
            self.timeAccum += elapsedTime

            if self.lastRuns.qsize() > wndsize:
                self.timeAccum -= self.lastRuns.get()

        def isReady(self):
            return self.lastRuns.qsize() >= wndsize

        def get(self) -> float:
            assert self.isReady()
            return self.timeAccum / self.lastRuns.qsize()

    call_time_stats = CallTimeStats()

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            return_value = func(*args, **kwargs)
            end_time = time.perf_counter()

            call_time_stats.updateTime(end_time - start_time)
            if call_time_stats.isReady():
                print(
                    'Mean execution time of', func.__name__,
                    'over', wndsize, 'runs is', call_time_stats.get()
                )

            return return_value

        return wrapper

    return decorator
