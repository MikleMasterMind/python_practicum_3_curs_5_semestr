def sheff(a, b):
    if not a and not b:
        return True
    if a and b:
        return False
    return a if a else b


import sys
exec(sys.stdin.read())