from itertools import tee, zip_longest
import sys


def seesaw(sequence):
    odd, even = tee(sequence)
    odd = (i for i in odd if i % 2 != 0)
    even = (i for i in even if i % 2 == 0)
    for e, o in zip_longest(even, odd):
        if e != None:
            yield e
        if o != None:
            yield o
        

exec(sys.stdin.read())