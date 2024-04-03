n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def backslash_dir_num(dir_num):
    if dir_num == 2:
        return 3
    if dir_num == 3:
        return 2
    if dir_num == 0:
        return 1
    if dir_num == 1:
        return 0

def go(x, y, dir_num):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    elapsed = 1

    while True:
        if arr[x][y] == 1:
            dir_num = 3 - dir_num
        elif arr[x][y] == 2:
            dir_num = backslash_dir_num(dir_num)

        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            elapsed += 1
        else:
            elapsed += 1
            break

    return elapsed

ans = 0

for i in range(n):
    dir_num = 1
    x, y = 0, i
    ans = max(ans, go(x, y, dir_num))

for i in range(n):
    dir_num = 2
    x, y = i, n - 1

    ans = max(ans, go(x, y, dir_num))

for i in range(n):
    dir_num = 3
    x, y = n - 1, i

    ans = max(ans, go(x, y, dir_num))

for i in range(n):
    dir_num = 0
    x, y = i, 0

    ans = max(ans, go(x, y, dir_num))

print(ans)