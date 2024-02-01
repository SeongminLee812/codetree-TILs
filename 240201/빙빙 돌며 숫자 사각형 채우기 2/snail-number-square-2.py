n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# function check if in range
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

dir_num = 0

x, y = 0, 0
a[x][y] = 1

for i in range(2, n * m + 1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny) or a[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x += dx[dir_num]
    y += dy[dir_num]
    a[x][y] = i

for line in a:
    print(" ".join(map(str, line)))