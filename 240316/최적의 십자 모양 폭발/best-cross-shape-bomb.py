import copy

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(target_arr, row, col):
    bomb_range = target_arr[row][col]
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    # 폭발이 시작된 위치부터 폭발
    target_arr[row][col] = 0

    for step in range(1, bomb_range):
        # 폭발 범위만큼 발자국 이동
        for dx, dy in zip(dxs, dys):
            nx = row + (dx * step)
            ny = col + (dy * step)
            if in_range(nx, ny):
                target_arr[nx][ny] = 0
    return target_arr

def push(target_arr):
    for col in range(n):
        temp_vertical = [0] * n
        temp_idx = n - 1
        for row in range(n - 1, -1, -1):
            if target_arr[row][col]:
                temp_vertical[temp_idx] = target_arr[row][col]
                temp_idx -= 1

        for rep_row in range(n):
            target_arr[rep_row][col] = temp_vertical[rep_row]

    return target_arr

def check_twin(target_arr):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if target_arr[i][j] == 0:
                continue
            if i < n - 1 and target_arr[i][j] == target_arr[i + 1][j]:
                cnt += 1
            if j < n - 1 and target_arr[i][j] == target_arr[i][j + 1]:
                cnt += 1

    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        # print()
        # print(f'====row: {i}, col: {j}====')
        new = copy.deepcopy(arr)
        new = bomb(new, i, j)
        # for line in new:
        #     print(' '.join(map(str, line)))
        # print('==')
        new = push(new)
        # for line in new:
        #     print(' '.join(map(str, line)))

        cnt = check_twin(new)
        # print(f'cnt: {cnt}')
        ans = max(ans, cnt)

print(ans)