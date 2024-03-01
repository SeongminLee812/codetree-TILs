n, t = map(int, input().split())

directions = input()
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# define dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir_num = 0

# check whether x, y in range or not
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# start position
x, y = n // 2, n // 2

total = 0
total += arr[x][y]

for d in directions:
    if d == 'R':
        dir_num = (dir_num + 1) % 4
    elif d == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    else:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny):
            total += arr[nx][ny]
            x, y = nx, ny

print(total)