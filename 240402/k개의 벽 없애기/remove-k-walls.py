import sys
from collections import deque

n, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

visited = [
    [False] * n
    for _ in range(n)
]

step = [
    [0] * n
    for _ in range(n)
]

walls = [
    (i, j)
    for i in range(n)
    for j in range(n)
        if arr[i][j] == 1
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

def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

def remove_wall(wall_list):
    for wall in wall_list:
        arr[wall[0]][wall[1]] = 0

def return_wall(wall_list):
    for wall in wall_list:
        arr[wall[0]][wall[1]] = 1


def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(x, y):
                push(nx, ny, step[x][y] + 1)

def choose(num_index, cnt):
    global ans
    if cnt == k:
        remove_wall(selected)
        bfs()
        if step[r2 - 1][c2 - 1]:
            ans = min(ans, step[r2 - 1][c2 - 1])
        return_wall(selected)
        return

    if num_index == n:
        return

    selected.append(num_index)
    choose(num_index + 1, cnt + 1)
    selected.pop()

    choose(num_index + 1, cnt)

q = deque()
selected = []
ans = sys.maxsize

choose(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)