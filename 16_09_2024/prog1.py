from math import *
def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return [-1]
            else:
                return [0]
        elif -c/b > 0:
            return [-sqrt(-c/b), sqrt(-c/b)]
        elif c == 0:
            return [0]
        else:
            return [0]
    else:
        d = b*b- 4 * a * c
        if d < 0:
            return [0]
        elif d == 0:
            x = -b / (2 * a)
            if x > 0:
                return [-sqrt(x), sqrt(x)]
            elif x == 0:
                return [0]
            else:
                return [0]
        else:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            ans = list()
            if x1 > 0:
                ans.append(sqrt(x1))
                ans.append(-sqrt(x1))
            elif x2 == 0:
                ans.append(0)
            if x2 > 0:
                ans.append(sqrt(x2))
                ans.append(-sqrt(x2))
            elif x2 == 0:
                ans.append(0)
            return sorted(ans) if len(ans) > 0 else [0]
            

if __name__ == '__main__':    
    a, b, c = map(float, input().split(','))
    print(*solve(a,b,c))