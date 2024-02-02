dir_num = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def turn_right(dir_num):
    dir_num = (dir_num + 1) % 4
    return dir_num

def turn_left(dir_num):
    dir_num = (dir_num - 1 + 4) % 4
    return dir_num

# input

n, t = map(int, input().split())
directions = list(input())

a = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

x, y = n // 2, n // 2

ans = a[x][y]

for d in directions:
    if d == 'R':
        dir_num = turn_right(dir_num)
    elif d == 'L':
        dir_num = turn_left(dir_num)
    else:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if not in_range(nx, ny):
            continue
        else:
            x = nx
            y = ny
            ans += a[x][y]

print(ans)