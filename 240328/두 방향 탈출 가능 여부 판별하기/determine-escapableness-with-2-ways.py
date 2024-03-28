n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

def dfs(x, y):
    dxs = [0, 1]
    dys = [1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

dfs(0, 0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)