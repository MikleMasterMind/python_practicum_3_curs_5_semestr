from itertools import cycle
import sys


def speed(path, stops, times):
    path = iter(path)
    stops = cycle(stops)
    times = iter(times)
    while True:
        sum_way = 0
        for _ in range(next(stops)):
            try:
                sum_way += next(path)
            except StopIteration:
                if sum_way:
                    try:
                        yield sum_way / next(times)
                    except StopIteration:
                        return
                return
        try:
            yield sum_way / next(times)
        except StopIteration:
            return

        
        
exec(sys.stdin.read())