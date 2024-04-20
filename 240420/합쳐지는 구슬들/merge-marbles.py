n, m, t = map(int, input().split())

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

dir_dict = {
    'U': 2,
    'R': 0,
    'L': 3,
    'D': 1
}

weight = [
    [0] * n
    for _ in range(n)
]

dir_arr = [
    [0] * n
    for _ in range(n)
]

ball_num = [
    [0] * n
    for _ in range(n)
]


for num in range(1, m + 1):
    r, c, d, w = input().split()
    r, c = int(r) - 1, int(c) - 1
    w = int(w)
    weight[r][c] = w
    dir_arr[r][c] = dir_dict[d]
    ball_num[r][c] = num

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def update(nx, ny, x, y, dir_num):
    new_weight[nx][ny] += weight[x][y]
    if new_ball_num[nx][ny] < ball_num[x][y]:
        new_ball_num[nx][ny] = ball_num[x][y]
        new_dir_arr[nx][ny] = dir_num

def move(x, y):
    dir_num = dir_arr[x][y]
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
        nx, ny = x, y
    update(nx, ny, x, y, dir_num)



for _ in range(t):
    new_weight = [
        [0] * n
        for _ in range(n)
    ]

    new_dir_arr = [
        [0] * n
        for _ in range(n)
    ]

    new_ball_num = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if ball_num[i][j]:
                move(i, j)


    for i in range(n):
        for j in range(n):
            weight[i][j] = new_weight[i][j]
            ball_num[i][j] = new_ball_num[i][j]
            dir_arr[i][j] = new_dir_arr[i][j]

num_of_ball = 0
max_weight = 0
for i in range(n):
    for j in range(n):
        if ball_num[i][j]:
            num_of_ball += 1
            max_weight = max(max_weight, weight[i][j])

print(num_of_ball, max_weight)