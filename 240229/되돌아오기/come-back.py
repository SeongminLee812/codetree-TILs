#     W   S  N  E
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y = 0, 0

dir_dict ={
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3
}

come_back = False
t = 0

n = int(input())
for _ in range(n):
    d, move_num = input().split()
    dir_num = dir_dict[d]
    move_num = int(move_num)

    for j in range(move_num):
        x, y = x + dx[dir_num], y + dy[dir_num]
        t += 1
        if x == 0 and y == 0:
            come_back = True
            break
    if come_back:
        break

if come_back:
    print(t)
else:
    print(-1)