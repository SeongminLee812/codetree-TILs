dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

x, y = 0, 0

directions = input()
dir_num = 0

for d in directions:
    if d == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif d == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)