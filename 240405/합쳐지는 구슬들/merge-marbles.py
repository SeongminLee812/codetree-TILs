n, m, t = map(int, input().split())

count = [
    [0] * n
    for _ in range(n)
]
weight = [
    [0] * n
    for _ in range(n)
]
nums = [
    [0] * n
    for _ in range(n)
]
dir_array = [
    [0] * n
    for _ in range(n)
]

for i in range(1, m + 1):
    direction_dir = {'U': 0, 'R': 2, 'L': 1, 'D': 3}
    r, c, direction, w = input().split()
    r, c, w = map(int, (r, c, w))
    r, c = r - 1, c - 1
    count[r][c] = 1
    weight[r][c] = w
    nums[r][c] = i
    dir_array[r][c] = direction_dir[direction]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(x, y):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    dir_num = dir_array[x][y]
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny):
        new_count[x][y] += 1
        new_weight[x][y] += weight[x][y]
        if new_nums[x][y] < nums[x][y]:
            new_nums[x][y] = nums[x][y]
            new_dir_array[x][y] = 3 - dir_array[x][y]
    else:
        new_count[nx][ny] += 1
        new_weight[nx][ny] += weight[x][y]
        if new_nums[nx][ny] < nums[x][y]:
            new_nums[nx][ny] = nums[x][y]
            new_dir_array[nx][ny] = dir_array[x][y]

def initialize():
    for i in range(n):
        for j in range(n):
            new_count[i][j] = 0
            new_nums[i][j] = 0
            new_weight[i][j] = 0
            new_dir_array[i][j] = 0


new_count = [
    [0] * n
    for _ in range(n)
]
new_nums = [
    [0] * n
    for _ in range(n)
]
new_weight = [
    [0] * n
    for _ in range(n)
]
new_dir_array = [
    [0] * n
    for _ in range(n)
]
for _ in range(t):
    initialize()
    for i in range(n):
        for j in range(n):
            if count[i][j]:
                move(i, j)
    for i in range(n):
        for j in range(n):
            if new_count[i][j] >= 2:
                new_count[i][j] = 1
            count[i][j] = new_count[i][j]
            nums[i][j] = new_nums[i][j]
            weight[i][j] = new_weight[i][j]
            dir_array[i][j] = new_dir_array[i][j]


max_weight = 0
final_count = 0
for i in range(n):
    for j in range(n):
        if count[i][j]:
            final_count += 1
            max_weight = max(max_weight, weight[i][j])

print(final_count, max_weight)