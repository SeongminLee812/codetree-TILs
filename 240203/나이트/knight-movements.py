from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False] * n for _ in range(n)]
step = [[-1] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

def push(x, y, v):
    global q, visited, step
    visited[x][y] = True
    q.append((x, y))
    step[x][y] = v + 1

def bfs():
    next_steps = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    while q:
        x, y = q.popleft()

        for (dx, dy) in next_steps:
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                v = step[x][y]
                push(nx, ny, v)

x, y = r1 - 1, c1 - 1
q = deque()
push(x, y, -1)
bfs()

if step[r2 - 1][c2 - 1] != -1:
    print(step[r2 - 1][c2 - 1])
else:
    print(-1)