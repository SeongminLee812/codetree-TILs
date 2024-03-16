n, m, t = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = map(int, input().split())
    count[r - 1][c - 1] = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    max_val = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and arr[nx][ny] > max_val:
            max_val = arr[nx][ny]
            max_pos = nx, ny

    next_x, next_y = max_pos
    next_count[next_x][next_y] += 1

while t:
    next_count = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if count[i][j]:
                move(i, j)

    for i in range(n):
        for j in range(n):
            if next_count[i][j] >= 2:
                next_count[i][j] = 0
            count[i][j] = next_count[i][j]

    t -= 1


ans = 0
for i in range(n):
    for j in range(n):
        if count[i][j]:
            ans += 1

print(ans)