stored = [[0 for __ in range(100)] for _ in range(100)]

while s:= input():
    n, m = eval(s)
    stored[n - 1][m - 1] += 1

for i, l in enumerate(stored):
    for j, v in enumerate(l):
        for _ in range(v):
            ans = f'{i + 1}, {j + 1}'
            print(ans)
