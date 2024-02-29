n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [
    [0] * m
    for _ in range(n)
]

dir_num = 0

x, y = 0, 0
arr[x][y] = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m
for i in range(2, n * m + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir_num = (dir_num + 1) % 4
        x, y = x + dx[dir_num], y + dy[dir_num]

    arr[x][y] = i

for row in arr:
    print(' '.join(map(str, row)))