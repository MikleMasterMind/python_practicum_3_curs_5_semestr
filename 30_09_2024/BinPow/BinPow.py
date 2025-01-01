def BinPow(a, n, f):
    if n == 1:
        return a
    if n % 2 == 0:
        dp = BinPow(a, n//2, f)
        return f(dp, dp)
    else:
        dp = BinPow(a, n - 1, f)
        return f(a, dp)

import sys
exec(sys.stdin.read())
