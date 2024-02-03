from collections import deque
import heapq

# get input
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, value):
    if not in_range(x, y):
        return False
    if a[x][y] >= value:
        return False
    if visited[x][y]:
        return False
    return True

def bfs(value):
    global q, visited
    global max_val, max_pos
    hq = []

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny, value):
                visited[nx][ny] = True
                q.append((nx, ny))
                if a[nx][ny] >= max_val:
                    max_val = a[nx][ny]
                    heapq.heappush(hq, (-a[nx][ny], nx, ny))
    if hq:
        return heapq.heappop(hq)
    else:
        return None


ans = (r - 1, c - 1)
x, y = r - 1, c - 1

for _ in range(k):
    q = deque()

    max_val = 0
    max_pos = []
    visited = [[False] * n for _ in range(n)]

    visited[x][y] = True
    q.append((x, y))
    value = a[x][y]
    hq = bfs(value)
    if not hq:
        break
    val, x, y = hq
    ans = x, y

print(ans[0] + 1, ans[1] + 1)