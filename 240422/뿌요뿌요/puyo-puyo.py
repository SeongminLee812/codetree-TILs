# 블럭의 수와, 최대 블럭의 크기 구함
# dfs 구현

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
    if not in_range(x, y) or visited[x][y]:
        return False
    if arr[x][y] != value:
        return False
    return True


def dfs(x, y):
    global blocks
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, arr[x][y]):
            visited[nx][ny] = True
            blocks += 1
            dfs(nx, ny)

boom = 0
max_blocks = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        blocks = 1
        visited[i][j] = True
        dfs(i, j)
        max_blocks = max(max_blocks, blocks)
        if blocks >= 4:
            boom += 1

print(boom, max_blocks)