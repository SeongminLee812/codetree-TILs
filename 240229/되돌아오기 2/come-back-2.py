dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

x, y = 0, 0
directions = input()

t = 0
come_back = False

for d in directions:
    t += 1
    if d == 'R':
        dir_num = (dir_num + 1) % 4
    elif d == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]
        if x == 0 and y == 0:
            come_back = True
            break

if come_back:
    print(t)
else:
    print(-1)