n, r, c = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def go(curr_r, curr_c):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    result_pos = (-1, -1)

    for dx, dy in zip(dxs, dys):
        nx = curr_r + dx
        ny = curr_c + dy
        if in_range(nx, ny) and arr[nx][ny] > arr[curr_r][curr_c]:
            result_pos = (nx, ny)
            return result_pos
    return result_pos

curr_r = r - 1
curr_c = c - 1
while True:
    print(arr[curr_r][curr_c], end=' ')
    next_pos = go(curr_r, curr_c)
    if next_pos == (-1, -1):
        break
    curr_r, curr_c = next_pos