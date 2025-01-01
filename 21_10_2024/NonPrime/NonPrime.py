import sys
from math import sqrt

def nonprime(n=0):
    res = n + 1
    while True:
        if res == 1:
            yield res
        for i in range(2, res):
            if res % i == 0:
                yield res
                break
            if i*i > res:
                break
        res += 1


exec(sys.stdin.read())