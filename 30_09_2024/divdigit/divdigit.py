def divdigit(N):
    count = 0
    for a in str(N):
        if int(a) != 0 and N % int(a) == 0:
            count += 1
    return count


import sys
exec(sys.stdin.read())