from collections import deque

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    global ice_cnt
    if not in_range(x, y) or visited[x][y]:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        ice_cnt += 1
        visited[x][y] = True
        return False
    return True

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

t = 0
last_ice = 1
while True:
    ice_cnt = 0
    visited = [
        [False] * m
        for _ in range(n)
    ]
    q = deque()
    visited[0][0] = True
    q.append((0, 0))
    bfs()

    if ice_cnt:
        last_ice = ice_cnt
        t += 1
    else:
        break

print(t, last_ice)