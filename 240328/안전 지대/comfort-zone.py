n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * m
    for _ in range(n)
]

max_height = 0
for line in arr:
    max_height = max(max_height, max(line))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] <= k:
        return False
    return True

def dfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

result_k = 1
result_area = 0

for k in range(1, max_height + 1):
    area = 0

    visited = [
        [False] * m
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] > k:
                area += 1
                visited[i][j] = True
                dfs(i, j)
    if area > result_area:
        result_k = k
        result_area = area

print(result_k, result_area)