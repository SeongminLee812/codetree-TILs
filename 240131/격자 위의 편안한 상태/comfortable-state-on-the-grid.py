n, m = map(int, input().split())

a = [[0] * (n + 1) for _ in range(n + 1)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return x > 0 and x <= n and y > 0 and y <= n

def comfortable(x, y):
    count = 0
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if in_range(nx, ny) and a[nx][ny] == 1:
            count += 1
    if count == 3:
        return True
    return False

for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    if comfortable(x, y):
        print(1)
    else:
        print(0)