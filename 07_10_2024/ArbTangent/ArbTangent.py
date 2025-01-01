import decimal
from decimal import Decimal


a = Decimal(input())
e = int(input())
decimal.getcontext().prec = e + 100

def chudnovsky(n):
    pi = Decimal(13591409)
    ak = Decimal(1)
    k = 1
    while k < n:
        ak *= -Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k*k*k*26680*640320*640320)
        val = ak*(13591409 + 545140134*k)
        pi += val
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


def sin(x):
    x %= 2 * pi
    result = x
    elem = x
    for n in range(1, 2000):  
        elem *= -x**2 / ((2 * n) * (2 * n + 1))
        result += elem
    return result


def cos(x):
    x %= 2 * pi
    result = 1
    elem = 1
    for n in range(1, 2000):  
        elem *=  -x**2 / ((2 * n - 1) * (2 * n))
        result += elem
    return result


pi = chudnovsky(e + 100)
radian = Decimal(a * pi / 200)
tan = Decimal(sin(radian) / cos(radian))
decimal.getcontext().prec = e
print(f'{tan:.{e}}')