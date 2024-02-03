from collections import deque

# input
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
step = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 0:
        return False
    return True

def push(x, y, v):
    global visited, q, step
    visited[x][y] = True
    q.append((x, y))
    step[x][y] = v

def bfs():
    global q, visited
    global step
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                v = step[x][y] + 1
                push(nx, ny, v)

q = deque()
push(0, 0, 0)
bfs()
if step[n - 1][m - 1]:
    print(step[n - 1][m - 1])
else:
    print(-1)