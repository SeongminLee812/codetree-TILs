from collections import deque

n, k = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

sick_mandarine = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if arr[i][j] == 2
]

visited = [
    [False] * n
    for _ in range(n)
]

steps = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] != 1:
        return False
    return True

def push(x, y, curr_step):
    visited[x][y] = True
    steps[x][y] = curr_step + 1
    q.append((x, y))

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, curr_step=steps[x][y])

q = deque()
for x, y in sick_mandarine:
    push(x, y, -1)

bfs()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            print(-1, end=' ')
        elif not visited[i][j]:
            print(-2, end=' ')
        else:
            print(steps[i][j], end=' ')
    print()