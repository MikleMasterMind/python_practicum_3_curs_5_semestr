from math import *
seq = set(eval(input()))
count = 0
mymax = max(seq)
sum_quares = set()
for x  in range(1, int((mymax)**0.5) + 1):
    for y in range(x, int((mymax - x*x)**0.5) + 1):
        for z in range(y, int((mymax - x*x - y*y)**0.5) + 1):
            sum_quares.add(x*x + y*y + z*z)
print(len(sum_quares & seq))