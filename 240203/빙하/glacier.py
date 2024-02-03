from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    global q, visited
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    ice_num = 0
    next = 0, 0

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if a[nx][ny] == 1:
                    visited[nx][ny] = True
                    ice_num += 1
                    a[nx][ny] = 0 # 녹이기
                    next = nx, ny
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return ice_num, next

last_ice_num = 0
t = 0

final_round = False

next = (0, 0)
visited = [[False] * m for _ in range(n)]
while not final_round:
    t += 1
    q = deque()
    q.append(next)
    now_ice_num, next = bfs()
    if now_ice_num != 0:
        last_ice_num = now_ice_num
    else:
        final_round = True



print(t - 1, last_ice_num)