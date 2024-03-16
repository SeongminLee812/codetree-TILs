t = int(input())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(x, y, dir_num):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if in_range(nx, ny):
        next_count[nx][ny] += 1
        next_directions[nx][ny] = dir_num
    else:
        dir_num = (dir_num + 2) % 4
        next_count[x][y] += 1
        next_directions[x][y] = dir_num

def reset_count():
    for i in range(n):
        for j in range(n):
            if next_count[i][j] >= 2:
                next_count[i][j] = 0
                next_directions[i][j] = 0
            count[i][j] = next_count[i][j]
            directions[i][j] = next_directions[i][j]

dir_dict = {
    'U': 2,
    'D': 0,
    'R': 1,
    'L': 3
}

for _ in range(t):
    n, m = map(int, input().split())
    count = [
        [0] * n
        for _ in range(n)
    ]
    directions = [
        [0] * n
        for _ in range(n)
    ]

    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1
        d = dir_dict[d]
        count[x][y] = 1
        directions[x][y] = d

    # 충분한 시간이 지나도록 반복 (한바퀴)
    for _ in range(n * 2):
        next_count = [
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

        reset_count()

    ans = 0
    for i in range(n):
        for j in range(n):
            ans += count[i][j]
    print(ans)