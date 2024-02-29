n, m = map(int, input().split())

arr = [
    [0] * m
    for _ in range(n)
]

# fill first position
x, y = 0, 0
arr[x][y] = 1

# define dx, dy
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir_num = 0

# check if x and y in range
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(2, n * m + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]
    arr[nx][ny] = i
    x, y = nx, ny

for line in arr:
    print(' '.join(map(str, line)))