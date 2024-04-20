n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def search(start_x, start_y, dir_num):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    t = 1
    x, y = start_x, start_y
    while True:
        if arr[x][y] == 1:
            dir_num = 3 - dir_num
        elif arr[x][y] == 2:
            if dir_num == 1:
                dir_num = 3
            elif dir_num == 3:
                dir_num = 1
            elif dir_num == 2:
                dir_num = 0
            else:
                dir_num = 2
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            t += 1
        else:
            return t + 1

ans = 0
for i in range(n):
    t = search(i, 0, 1)
    ans = max(ans, t)
for i in range(n):
    t = search(0, i, 3)
    ans = max(ans, t)
for i in range(n):
    t = search(i, n - 1, 0)
    ans = max(ans, t)
for i in range(n):
    t = search(n - 1, i, 2)
    ans = max(ans, t)

print(ans)