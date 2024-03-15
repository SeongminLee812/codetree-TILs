# 1. 우선 폭탄을 터뜨리고 터진 공간은 0으로 표시함.
# 2. 터진 공간(요소가 0인 부분)은 중력으로 당겨주기

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
row, col = map(int, input().split())
row -= 1
col -= 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(row, col):
    # 폭발
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    bomb_range = arr[row][col]
    arr[row][col] = 0

    for now_range in range(bomb_range):
        for dx, dy in zip(dxs, dys):
            nx = row + (dx * now_range)
            ny = col + (dy * now_range)
            if in_range(nx, ny):
                arr[nx][ny] = 0


def shift_down():
    # 중력에 의해서 내려오는 함수
    for col in range(n):
        temp_array = [0] * n
        temp_idx = 0

        for row in range(n - 1, -1, -1):
            if arr[row][col]:
                temp_array[temp_idx] = arr[row][col]
                temp_idx += 1

        end_of_temp_array = temp_idx
        temp_idx = 0

        for row in range(n - 1, -1, -1):
            if temp_idx >= end_of_temp_array:
                arr[row][col] = 0
            else:
                arr[row][col] = temp_array[temp_idx]
                temp_idx += 1


bomb(row, col)
shift_down()

for line in arr:
    print(' '.join(map(str, line)))