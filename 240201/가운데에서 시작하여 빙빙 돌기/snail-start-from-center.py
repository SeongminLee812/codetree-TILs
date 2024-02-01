n = int(input())
a = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dir_num = -1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

dist = 1
x, y = n // 2, n // 2
a[x][y] = 1
times = 0
count = 1

while a[n - 1][n - 1] == 0:

    dir_num = (dir_num + 1) % 4
    for _ in range(dist):
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny) and a[nx][ny] == 0:
            a[nx][ny] = a[x][y] + 1
            x, y = nx, ny

    if count == 2:
        count = 1
        dist += 1
    else:
        count += 1

for line in a:
    print(' '.join(map(str, line)))