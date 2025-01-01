import sys
from string import ascii_letters
from functools import wraps


class Pairs:
    __slots__ = tuple(ascii_letters)

    def __init__(self, n):
        for c in ascii_letters:
            setattr(self, c, n)
            n = n + 1 if n % 52 != 0 else 1 

    @wraps(str)
    def __str__(self):
        order = ' '.join(sorted(ascii_letters, key=lambda c: getattr(self, c)))
        return order


exec(sys.stdin.read())