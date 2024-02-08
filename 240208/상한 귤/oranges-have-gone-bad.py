from collections import deque

n, k = map(int, input().split())
a = [list(map(int, input().split()))
     for _ in range(n)]
steps = [[0] * n
         for _ in range(n)]
visited = [[False] * n
           for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] != 1:
        return False
    return True


def bfs():
    global visited, steps
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                steps[nx][ny] = steps[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

q = deque()
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            q.append((i, j))

bfs()

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            print(-1, end=' ')
        elif a[i][j] == 1:
            if visited[i][j]:
                print(steps[i][j], end=' ')
            else:
                print(-2, end=' ')
        else:
            print(0, end=' ')
    print()