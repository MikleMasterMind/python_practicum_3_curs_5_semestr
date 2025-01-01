

def solve():
    s = input()
    max_x, max_y, max_z = map(float, s.split(','))
    min_x, min_y, min_z = max_x, max_y, max_z
    while s != '…' and s != '':
        x, y, z = map(float, s.split(','))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        s = input()
    v = (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
    print(v)

solve()