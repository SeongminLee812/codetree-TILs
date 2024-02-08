n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, nx, ny):
    if not in_range(nx, ny):
        return False
    if visited[nx][ny]:
        return False
    if a[nx][ny] != a[x][y]:
        return False
    return True

def dfs(x, y):
    global blocks

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(x, y, nx, ny):
            blocks += 1
            visited[nx][ny] = True
            dfs(nx, ny)

bomb = 0
max_block = 1

for i in range(n):
    for j in range(n):
        blocks = 1
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
        if blocks >= 4:
            bomb += 1
        max_block = max(max_block, blocks)

print(bomb, max_block)