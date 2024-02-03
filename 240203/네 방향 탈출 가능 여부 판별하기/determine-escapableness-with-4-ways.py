from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 0:
        return False
    return True

def push(x, y):
    global q, visited
    visited[x][y] = True
    q.append((x, y))

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def bfs():
    global q, visited
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                push(nx, ny)

q = deque()
if can_go(0, 0):
    push(0, 0)
bfs()

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)