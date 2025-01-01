import time

def compare(less: tuple, greater: tuple) -> bool: 
    max_l = max(less)
    min_l = min(less)
    mid_l = sum(less) - max_l - min_l
    max_g = max(greater)
    min_g = min(greater)
    mid_g = sum(greater) - max_g - min_g
    return min_l <= min_g and mid_l <= mid_g and max_l <= max_g and \
        (min_l != min_g or mid_l != mid_g or max_l != max_g)


def solve1(l: list):
    for i in range(len(l)):
        for j in range(i, len(l)):
            var = l[j]
            for k in l[j+1:]:
                if compare(var, k):
                    break
            else:
                l.pop(j)
                l.insert(i, var)
                break
    return l

   
unsorted = list()
while s := input():
    unsorted.append(tuple(map(int, s.split(','))))

ans = solve1(unsorted)
for i in ans:
    print(*i, sep=', ')
