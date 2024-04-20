import copy

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def boom(x, y, boom_range):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    new_arr[x][y] = 0
    for i in range(1, boom_range + 1):
        for dx, dy in zip(dxs, dys):
            nx = x + dx * i
            ny = y + dy * i
            if in_range(nx, ny):
                new_arr[nx][ny] = 0

def move_down():
    for col in range(n):

        temp_arr = [0] * n
        temp_idx = n - 1
        for row in range(n - 1, -1, -1):
            if new_arr[row][col] != 0:
                temp_arr[temp_idx] = new_arr[row][col]
                temp_idx -= 1

        for idx in range(n):
            new_arr[idx][col] = temp_arr[idx]

def check_pair():
    result = 0
    for i in range(n):
        for j in range(n):
            if new_arr[i][j] == 0:
                continue
            if i < n - 1 and new_arr[i][j] == new_arr[i + 1][j]:
                result += 1
            if j < n - 1 and new_arr[i][j] == new_arr[i][j + 1]:
                result += 1
    return result

ans = 0
for i in range(n):
    for j in range(n):
        new_arr = copy.deepcopy(arr)
        boom(i, j, new_arr[i][j])
        move_down()
        ans = max(ans, check_pair())

print(ans)