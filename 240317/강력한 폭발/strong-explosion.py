n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
boom_count = 0

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            boom_count += 1

def choose(index):
    global ans
    if index == boom_count + 1:
        cnt = simulate()
        ans = max(ans, cnt)
        return

    for i in range(1, 4):
        boom_list.append(i)
        choose(index + 1)
        boom_list.pop()

def simulate():
    global ans
    area = [
        [0] * n
        for _ in range(n)
    ]

    idx = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                boom_num = boom_list[idx]
                bomb(i, j, boom_num, area)
                idx += 1

    global_count = sum([
        area[i][j] for i in range(n) for j in range(n)
    ])

    return global_count

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(x, y, boom_type, area):
    if boom_type == 1:
        dxs = [-2, -1, 0, 1, 2]
        dys = [0, 0, 0, 0, 0]
    elif boom_type == 2:
        dxs = [0, -1, 0, 1, 0]
        dys = [0, 0, 1, 0, -1]
    else:
        dxs = [0, -1, -1, 1, 1]
        dys = [0, -1, 1, 1, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            area[nx][ny] = 1



boom_list = []
ans = 0

choose(1)
print(ans)