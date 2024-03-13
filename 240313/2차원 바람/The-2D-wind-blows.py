import copy

def shifting(arr, r1, c1, r2, c2):
    # 가장 위의 줄 밀기
    top_right = arr[r1][c2]
    for i in range(c2, c1, -1):
        arr[r1][i] = arr[r1][i - 1]

    # push right col
    bottom_right = arr[r2][c2]
    for r in range(r2, r1 + 1, -1):
        arr[r][c2] = arr[r - 1][c2]
    arr[r1 + 1][c2] = top_right

    # push bottom
    bottom_left = arr[r2][c1]
    for c in range(c1, c2 - 1):
        arr[r2][c] = arr[r2][c + 1]
    arr[r2][c2 - 1] = bottom_right

    # left colomn
    for r in range(r1, r2 - 1):
        arr[r][c1] = arr[r + 1][c1]
    arr[r2 - 1][c1] = bottom_left

    return arr

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def near_average(arr, x, y):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    total = arr[x][y]
    in_range_cnt = 1

    for dx, dy in zip(dxs, dys):
        nx = x - dx
        ny = y - dy
        if in_range(nx, ny):
            total += arr[nx][ny]
            in_range_cnt += 1
    return total // in_range_cnt

def averaging(arr, r1, c1, r2, c2):
    avg_arr = copy.deepcopy(arr)

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            avg_arr[r][c] = near_average(arr, r, c)
    return avg_arr


if __name__ == '__main__':
    n, m, q = map(int, input().split())

    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        arr = shifting(arr, r1, c1, r2, c2)
        arr = averaging(arr, r1, c1, r2, c2)

for line in arr:
    print(' '.join(map(str, line)))