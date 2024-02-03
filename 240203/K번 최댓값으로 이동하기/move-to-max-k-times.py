from collections import deque

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

def push(x, y):
    global q, visited
    visited[x][y] = True
    q.append((x, y))

def bfs(value):
    global q, visited
    global max_val, max_pos

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, value):
                push(nx, ny)
                max_val = max(max_val, a[nx][ny]) #처음 탐색한 곳은 max_val이 0이므로 들어가 버림

    for i in range(n):
        for j in range(n):
            if a[i][j] == max_val:
                max_pos.append((i, j))

q = deque()
q.append((r - 1, c - 1))
ans = (r - 1, c - 1)

for _ in range(k):
    max_val = 0
    max_pos = []
    visited = [[False] * n for _ in range(n)]
    x, y = q[0]
    print(f'{_ + 1} init : \tx={x} y={y}')
    visited[x][y] = True
    value = a[x][y]
    bfs(value)
    if not max_pos:
        break
    max_pos.sort(key=lambda temp: (temp[0], temp[1]))
    push(*max_pos[0])
    ans = max_pos[0]

print(ans[0] + 1, ans[1] + 1)