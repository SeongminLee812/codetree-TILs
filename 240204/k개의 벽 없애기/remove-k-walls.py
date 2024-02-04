from itertools import combinations
from collections import deque
import copy

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

wall = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            wall.append((i, j))

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or matrix[x][y] == 1:
        return False
    return True

def initialize():
    visited = [[False] * n for _ in range(n)]
    matrix = copy.deepcopy(a)
    step = [[0] * n for _ in range(n)]
    return visited, matrix, step

def bfs():
    global q, visited, step
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

all_com = combinations(wall, k)

min_step = 1e10

for remove_walls in all_com:
    visited, matrix, step = initialize()
    for i, j in remove_walls:
        matrix[i][j] = 0

    q = deque()
    q.append((r1, c1))
    visited[r1][c1] = True
    bfs()
    if step[r2][c2]:
        min_step = min(min_step, step[r2][c2])

if min_step == 1e10:
    print(-1)
else:
    print(min_step)