n = int(input())

arr = [
    [0] * n
    for _ in range(n)
]

# start position
x, y = n // 2, n // 2
arr[x][y] = 1

# check whether x, y in range or not
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# define dx, dy
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dir_num = 0
move_num = 1

i = 2
limit = n * n

turn = 0
while i < limit:
    if turn == 2:
        move_num += 1
        turn = 0
    for _ in range(move_num):
        x, y = x + dx[dir_num], y + dy[dir_num]
        arr[x][y] = i
        i += 1
        if i > limit:
            break


    dir_num = (dir_num + 1) % 4
    turn += 1

for line in arr:
    print(' '.join(map(str, line)))