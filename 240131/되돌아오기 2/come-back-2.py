dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
ans = -1
t = 0
x, y = 0, 0

directs = input()

for d in directs:
    if d == 'F':
        x += dx[dir_num]
        y += dy[dir_num]
    elif d == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif d == 'R':
        dir_num = (dir_num + 1) % 4
    t += 1
    if x == 0 and y == 0:
        ans = t
        break
print(ans)