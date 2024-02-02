# input
n, m =  map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, 0]
dys = [0, 1]

visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    return in_range(x, y) and a[x][y] == 1 and visited[x][y] == False

def dfs(x, y):
    a[x][y] = 2
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)


if a[n - 1][m - 1] == 2:
    print(1)
else:
    print(0)