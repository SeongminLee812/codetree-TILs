import copy

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(x, y, original_array):
    result = copy.deepcopy(original_array)
    bomb_range = result[x][y]
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    bomb_range[x][y] = 0

    for br in range(1, bomb_range):
        for dx, dy in zip(dxs, dys):
            nx = x + dx * br
            ny = y + dy * br
            if in_range(nx, ny):
                result[nx][ny] = 0
    return result

def gratify(local_array):
    for col in range(n):
        temp = [0] * n
        temp_index = n - 1
        for row in range(n - 1, -1, -1):
            if local_array[row][col]:
                temp[temp_index] = local_array[row][col]
                temp_index -= 1
        for i in range(n):
            local_array[i][col] = temp[i]
    return local_array

def calc(local_array):
    cnt = 0
    # 열방향 검사
    for i in range(n):
        for j in range(n - 1):
            if local_array[i][j] == 0:
                continue
            if local_array[i][j] == local_array[i][j + 1]:
                cnt += 1
    # 행방향 검사
    for i in range(n - 1):
        for j in range(n):
            if local_array[i][j] == 0:
                continue
            if local_array[i][j] == local_array[i + 1][j]:
                cnt += 1

    return cnt

def find_max(x, y):
    global ans
    bomb_array = bomb(x, y, arr)
    bomb_array = gratify(bomb_array)
    ans = max(ans, calc(bomb_array))

ans = 0
for i in range(n):
    for j in range(n):
        find_max(i, j)

print(ans)