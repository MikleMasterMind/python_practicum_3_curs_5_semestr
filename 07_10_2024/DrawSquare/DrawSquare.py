def squares(w, h, *boxes):
    res = ['.' * w for _ in range(h)]
    for box in boxes:
        x, y, s, c = box
        for i in range(y, y + s):
            res[i] = res[i][:x] + c * s + res[i][x + s:]
    for line in res:
        print(line)

import sys
exec(sys.stdin.read())