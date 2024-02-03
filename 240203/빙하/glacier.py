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

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if a[nx][ny] == 1:
                    visited[nx][ny] = True
                    ice_num += 1
                    a[nx][ny] = 0 # 녹이기
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return ice_num

last_ice_num = 0
t = 0

final_round = False

while not final_round:
    t += 1
    q = deque()
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(m):
                if not visited[i][j]:
                    q.append((i, j))
                    now_ice_num = bfs()
                    if now_ice_num != 0:
                        last_ice_num = now_ice_num
                    else:
                        final_round = True

        else:
            for j in [0, m - 1]:
                if not visited[i][j]:
                    q.append((i, j))
                    now_ice_num = bfs()
                    if now_ice_num != 0:
                        last_ice_num = now_ice_num
                    else:
                        final_round = False

print(t - 1, last_ice_num)