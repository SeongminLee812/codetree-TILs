# 반대로 쉘터에서 사람에 도착하는 것을 구하면 됨
# 쉘터를 전부 큐에 넣고 시작하면, 가장 최단거리로 사람이 있는 곳에 도달할 수 있음
# 쉘터로부터의 step을 전부 기억하고, 사람이 있는, a[x][y] == 2인 곳만 그대로 step을 작성하면 됨

from collections import deque

n, h, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, visited):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if a[x][y] == 1:
        return False
    return True

def bfs():
    global q, visited, steps

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, visited):
                visited[nx][ny] = True
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))
    return -1

q = deque()
for i in range(n):
    for j in range(n):
        if a[i][j] == 3:
            q.append((i, j))

# 정답 행렬
ans = [[0] * n for _ in range(n)]

# 필요한 배열
steps = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

bfs()

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            if steps[i][j]:
                print(steps[i][j], end=' ')
            else:
                print(-1, end=' ')
        else:
            print(0, end=' ')
    print()