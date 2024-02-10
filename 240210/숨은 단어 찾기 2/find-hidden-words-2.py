n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def check(x, y):
    global total
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    for dx, dy in zip(dxs, dys):
        curr_x = x
        curr_y = y
        move = 1
        ok = True
        while move < 3:
            nx, ny = curr_x + dx, curr_y + dy
            if not in_range(nx, ny) or arr[nx][ny] != 'E':
                ok = False
                break
            move += 1
            curr_x, curr_y = nx, ny
        if ok:
            total += 1

total = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            check(i, j)
print(total)