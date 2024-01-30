dir_num = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y = 0, 0

directs = input()
for d in directs:
    if d == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif d == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)