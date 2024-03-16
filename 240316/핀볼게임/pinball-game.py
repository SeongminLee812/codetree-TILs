n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
pr_dict = {
    0: '<-',
    1: '↑',
    2: '↓',
    3: '->'
}

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def go(x, y):
    global dir_num
    elapsed_time = 1
    # print('====')
    while True:
        pin = arr[x][y]
        # print(x, y, pr_dict[dir_num], pin)
        if pin == 1:
            dir_num = (dir_num + 2) % 4
        elif pin == 2:
            if dir_num == 2:
                dir_num = 3
            elif dir_num == 3:
                dir_num = 2
            elif dir_num == 1:
                dir_num = 0
            else:
                dir_num = 1
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        elapsed_time += 1
        if in_range(nx, ny):
            x, y = nx, ny
        else:
            break
    return elapsed_time

ans = 0
for i in range(n * 4):
    line = i // n
    if line == 0:
        x, y = 0, i % n
        dir_num = 2
        cnt = go(x, y)
        ans = max(ans, cnt)

    elif line == 1:
        x, y = i % n, n - 1
        dir_num = 0
        cnt = go(x, y)
        ans = max(ans, cnt)
    elif line == 2:
        x, y = n - 1, i % n
        dir_num = 1
        cnt = go(x, y)
        ans = max(ans, cnt)
    else:
        x, y = i % n, 0
        dir_num = 3
        cnt = go(x, y)
        ans = max(ans, cnt)

print(ans)