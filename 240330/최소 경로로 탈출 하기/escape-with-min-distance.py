from collections import deque

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

step = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] != 1:
        return False
    return True

def push(x, y, s):
    visited[x][y] = True
    step[x][y] = s
    q.append((x, y))

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)


q = deque()
q.append((0, 0))
bfs()

if step[n - 1][m - 1]:
    print(step[n - 1][m - 1])
else:
    print(-1)