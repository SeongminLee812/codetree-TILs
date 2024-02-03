from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

all_point = ((i, j) for i in range(n) for j in range(n))
all_start = combinations(all_point, k)

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, diff):
    if diff < u or diff > d:
        return False
    if visited[x][y]:
        return False
    return True

def bfs():
    global q, visited
    global go_city
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        # print(f'x={x} y={y}')
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                diff = abs(a[x][y] - a[nx][ny])
                if can_go(nx, ny, diff):
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    go_city += 1

max_go_city = 0

for iter, start in enumerate(all_start):
    # 모든 경우의 수 탐색
    visited = [[False] * n for _ in range(n)]
    q = deque()
    go_city = 0
    # print('#' * 15, iter, '#' * 15)
    for i, j in start:
        # 경우의 수 내에서 좌표 탐색
        # print(f'###### start = {i}, {j}')
        if not visited[i][j]:
            visited[i][j] = True
            q.append((i, j))
            go_city += 1
            bfs()
    max_go_city = max(max_go_city, go_city)

print(max_go_city)