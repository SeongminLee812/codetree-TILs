from collections import deque

n, h, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

step = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 1:
        return False
    return True

def push(x, y, s):
    visited[x][y] = True
    q.append((x, y))
    step[x][y] = s

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

# initailize q
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 3:
            visited[i][j] = True
            q.append((i, j))

bfs()
# print output
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            if step[i][j]:
                print(step[i][j], end=' ')
            else:
                print(-1, end=' ')
        else:
            print(0, end=' ')
    print()