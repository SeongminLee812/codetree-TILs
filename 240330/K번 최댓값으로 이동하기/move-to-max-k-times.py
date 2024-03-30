from collections import deque

n, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(int, input().split())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] >= threshold:
        return False
    return True

def bfs():
    global next_x, next_y
    global max_val

    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

                # max 값 갱신
                if (arr[nx][ny], -nx, -ny) > (max_val, -next_x, -next_y):
                    next_x, next_y = nx, ny
                    max_val = arr[nx][ny]

x, y = r - 1, c - 1
next_x, next_y = x, y
q = deque()


for _ in range(k):
    # initialization
    visited = [
        [False] * n
        for _ in range(n)
    ]
    max_val = 0
    threshold = arr[x][y]

    visited[x][y] = True
    q.append((x, y))
    bfs()

    if next_x == x and next_y == y:
        break
    else:
        x, y = next_x, next_y

print(x + 1, y + 1)