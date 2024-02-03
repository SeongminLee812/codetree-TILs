from collections import deque

n, h, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, visited):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if a[x][y] == 1:
        return False
    return True

def bfs(x, y):
    steps = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    q = deque()
    visited[x][y] = True
    q.append((x, y))

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, visited):
                visited[nx][ny] = True
                steps[nx][ny] = steps[x][y] + 1
                if a[nx][ny] == 3:
                    return steps[nx][ny]
                q.append((nx, ny))
    return -1

global_q = deque()
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            global_q.append((i, j))

# 정답 행렬
ans = [[0] * n for _ in range(n)]

while global_q:
    start_x, start_y = global_q.popleft()
    step_num = bfs(start_x, start_y)
    ans[start_x][start_y] = step_num

for line in ans:
    print(" ".join(map(str, line)))