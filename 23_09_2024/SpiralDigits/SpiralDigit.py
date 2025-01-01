def solve(m, n):
    field = [[-1] * m for _ in range(n)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    symb = 0
    i = 0
    index_x, index_y = 0, 0
    d_x, d_y = direction[i][0], direction[i][1]
    while True:
        field[index_x][index_y] = symb
        symb = (symb + 1) % 10
        if (index_x + d_x >= n or index_y + d_y >= m) \
            or field[index_x + d_x][index_y + d_y] != -1:
            i = (i + 1) % 4
            d_x, d_y = direction[i][0], direction[i][1]
            if (index_x + d_x >= n or index_y + d_y >= m) \
                or field[index_x + d_x][index_y + d_y] != -1:
                break
        index_x += d_x
        index_y += d_y
    return field

m, n = map(int, input().split(','))
field = solve(m, n)
for f in field:
    print(*f)
