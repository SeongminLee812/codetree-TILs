n, m = map(int, input().split())

arr = [
    [0] * m
    for _ in range(n)
]
# fill start position
start = ord('A')
end = ord('Z')
x, y = 0, 0
arr[x][y] = chr(start)

# check whether x, y in range or not
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

# define dx, dy
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num = 0

fill_num = start

for _ in range(n * m - 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]

    fill_num += 1
    if fill_num > end:
        fill_num = start

    arr[nx][ny] = chr(fill_num)
    x, y = nx, ny

for line in arr:
    print(' '.join(line))