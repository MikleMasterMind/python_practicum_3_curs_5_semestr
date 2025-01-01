import sys
from functools import wraps


class Fix:
    def __init__(self, n):
        self.round_n = n

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwards):
            good_args = []
            for arg in args:
                if type(arg) == float:
                    arg = round(arg, self.round_n)
                good_args.append(arg)
            good_kwards = {}
            for kward in kwards:
                a = kwards[kward]
                if type(a) == float:
                    a = round(a, self.round_n)
                good_kwards[kward] = a
            result = f(*good_args, **good_kwards)
            if type(result) == float:
                result = round(result, self.round_n)
            return result
        return wrapper


exec(sys.stdin.read()) 