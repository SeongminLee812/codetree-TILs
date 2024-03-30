from collections import deque
n, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

candidate = []

for _ in range(k):
    r, c = map(int, input().split())
    candidate.append((r - 1, c - 1))

visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] != 0:
        return False
    return True

def bfs():
    global block

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                block += 1
                q.append((nx, ny))

block = 0
q = deque()
for x, y in candidate:
    if can_go(x, y):
        visited[x][y] = True
        block += 1
        q.append((x, y))
bfs()
print(block)