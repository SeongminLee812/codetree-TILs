from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [
    [False] * n
    for _ in range(n)
]
step = [
    [0] * n
    for _ in range(n)
]

q = deque()
q.append((r1 - 1, c1 - 1))
visited[r1 - 1][c1 - 1] = True

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y) or visited[x][y]:
        return False
    return True

def push(x, y, s):
    visited[x][y] = True
    step[x][y] = s
    q.append((x, y))

def bfs():
    dxs = [-2, -2, -1, 1, 2, 2, 1, -1]
    dys = [-1, 1, 2, 2, 1, -1, -2, -2]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

bfs()

end = step[r2 - 1][c2 - 1]
if not end and not visited[r2 - 1][c2 - 1]:
    print(-1)
else:
    print(end)