n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def search(num):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                return i, j

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def change(x, y):
    dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
    dys = [-1, 0, 1, 1, 1, 0, -1, -1]
    max_val = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] > max_val:
            max_val = arr[nx][ny]
            max_pos = nx, ny

    next_x, next_y = max_pos
    arr[x][y], arr[next_x][next_y] = arr[next_x][next_y], arr[x][y]

while m:
    for num in range(1, n * n + 1):
        x, y = search(num)
        change(x, y)
    m -= 1

for line in arr:
    print(' '.join(map(str, line)))