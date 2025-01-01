from math import *

def solve(n):
    count = 0
    for i in range(2, int(sqrt(n)) + 1):
        for j in range(2, int(log2(n)) + 1):
            m = i ** j
            count += 1
            if m > n:
                break
            if m == n:
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    print(solve(int(input())))