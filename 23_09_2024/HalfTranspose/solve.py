if s := input():
    matrix = [[int(i) for i in s.split(',')]]
else:
    exit()
n = len(matrix[0])
for _ in range(n - 1):
    matrix.append([int(i) for i in input().split(',')])

print(matrix[0][0])

for k in range(1, n):
    for i in range(k):
        print(matrix[k][i], end=',')
    for i in range(k, 0, -1):
        print(matrix[i][k], end=',')
    print(matrix[0][k])
