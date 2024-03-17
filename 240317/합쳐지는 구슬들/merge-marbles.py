n, m, t = map(int, input().split())

count = [
    [0] * n
    for _ in range(n)
]
weight = [
    [0] * n
    for _ in range(n)
]
numbers = [
    [0] * n
    for _ in range(n)
]
directions = [
    [0] * n
    for _ in range(n)
]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

mapping = {
    'U': 0,
    'L': 1,
    'D': 3,
    'R': 2
}

for num in range(1, m + 1):
    r, c, d, w = input().split()
    r, c = int(r) - 1, int(c) - 1
    d = mapping[d]
    w = int(w)

    count[r][c] = 1
    weight[r][c] = w
    directions[r][c] = d
    numbers[r][c] = num

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(x, y, dir_num):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    number = numbers[x][y]

    if in_range(nx, ny):
        next_count[nx][ny] += 1
        next_weight[nx][ny] += weight[x][y]
        if next_numbers[nx][ny] < number:
            next_numbers[nx][ny] = number
            next_directions[nx][ny] = dir_num
    else:
        dir_num = 3 - dir_num
        next_count[x][y] += 1
        next_weight[x][y] += weight[x][y]
        if next_numbers[x][y] < number:
            next_numbers[x][y] = number
            next_directions[x][y] = dir_num


def reset():
    for i in range(n):
        for j in range(n):
            _count = 1 if next_count[i][j] >= 1 else 0
            count[i][j] = _count
            weight[i][j] = next_weight[i][j]
            numbers[i][j] = next_numbers[i][j]
            directions[i][j] = next_directions[i][j]

for _ in range(t):
    # print('========')
    # for line in weight:
    #     print(' '.join(map(str, line)))
    next_count = [
        [0] * n
        for _ in range(n)
    ]
    next_weight = [
        [0] * n
        for _ in range(n)
    ]
    next_numbers = [
        [0] * n
        for _ in range(n)
    ]
    next_directions = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if count[i][j]:
                move(i, j, directions[i][j])
    reset()
# 
# 
# print('========')
# for line in weight:
#     print(' '.join(map(str, line)))

print(sum([
    count[i][j] for i in range(n) for j in range(n)
]), end=' ')
print(max([
    weight[i][j] for i in range(n) for j in range(n)
]
))