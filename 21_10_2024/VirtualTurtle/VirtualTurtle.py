import sys


def turtle(coord, direction):
    cur_x, cur_y = coord
    directions = {0: (1, 0), 1: (0,  1), 2: (-1, 0), 3: (0, -1)}
    cur_dir = directions[direction]
    cur_cmd = yield
    while True:
        if cur_cmd == 'f':
            cur_x += cur_dir[0]
            cur_y += cur_dir[1]
        else:
            direction = (direction + 1) % 4 if cur_cmd == 'l' else (direction - 1) % 4
            cur_dir = directions[direction]
        cur_cmd = yield (cur_x, cur_y)
        

exec(sys.stdin.read())