from collections import deque

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# initialize visited array
visited = [[False] * n for _ in range(n)]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 1:
        return False
    return True

def push(x, y):
    global q, visited
    visited[x][y] = True
    q.append((x, y))

q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    push(r - 1, c - 1)

total = 0

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    total += 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            push(nx, ny)


print(total)