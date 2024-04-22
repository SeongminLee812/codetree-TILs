import sys
from collections import deque

n, k, u, d = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

citys = [
    (i, j)
    for i in range(n)
    for j in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, value):
    if not in_range(x, y):
        return False
    if abs(arr[x][y] - value) < u or abs(arr[x][y] - value) > d:
        return False
    if visited[x][y]:
        return False
    return True

def push(x, y):
    global num_of_adj_city
    q.append((x, y))
    visited[x][y] = True
    num_of_adj_city += 1

def bfs():
    global num_of_adj_city
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, arr[x][y]):
                push(nx, ny)
    return num_of_adj_city

def choose(num_index, cnt):
    global ans
    if cnt == k + 1:
        candidate.append(selected[:])
        return

    if num_index == len(citys):
        return

    selected.append(num_index)
    choose(num_index + 1, cnt + 1)
    selected.pop()

    choose(num_index + 1, cnt)


selected = []
candidate = []
ans = -sys.maxsize

choose(0, 1)

for s in candidate:
    q = deque()
    visited = [
        [False] * n
        for _ in range(n)
    ]
    num_of_adj_city = 0

    for i in s:
        x, y = citys[i]
        push(x, y)
    bfs()
    ans = max(ans, num_of_adj_city)

print(ans)