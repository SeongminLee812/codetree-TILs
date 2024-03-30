from collections import deque

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    global ice_cnt, last_ice_pos, ice_q
    if not in_range(x, y) or visited[x][y]:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        ice_cnt += 1
        visited[x][y] = True
        ice_q.append((x, y))
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
last_ice_cnt = 1
last_ice_pos = 0, 0
ice_q = deque()
visited = [
    [False] * m
    for _ in range(n)
]

ice_q.append((0, 0))

while True:
    ice_cnt = 0
    for x, y in ice_q:
        visited[x][y] = True
    q = ice_q
    ice_q = deque()
    bfs()

    if ice_cnt:
        last_ice_cnt = ice_cnt
        t += 1
    else:
        break

print(t, last_ice_cnt)