n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, value):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] != value:
        return False
    return True

def dfs(x, y, value):
    global blocks

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, value):
            visited[nx][ny] = True
            blocks += 1
            dfs(nx, ny, value)


bomb = 0
max_blocks = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            blocks = 1
            visited[i][j] = True
            dfs(i, j, arr[i][j])
            if blocks >= 4:
                bomb += 1
            max_blocks = max(max_blocks, blocks)

print(bomb, max_blocks)