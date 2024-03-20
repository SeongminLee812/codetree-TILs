n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dir_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())

def get_dxdy(dir_num):
    dxs = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    return dxs[dir_num], dys[dir_num]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def choose(curr_x, curr_y, cnt):
    global ans

    dir_num = dir_arr[curr_x][curr_y]
    dx, dy = get_dxdy(dir_num)
    curr_num = arr[curr_x][curr_y]

    for i in range(1, n):
        nx, ny = curr_x + (i * dx), curr_y + (i * dy)
        if in_range(nx, ny) and arr[nx][ny] > curr_num:
            choose(nx, ny, cnt + 1)
        else:
            ans = max(ans, cnt)


ans = 0
choose(r - 1, c - 1, 0)
print(ans)