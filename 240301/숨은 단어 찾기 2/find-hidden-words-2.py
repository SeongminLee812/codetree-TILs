# 8 direction
dxs = [
    [0, 1, 2], # down
    [0, -1, -2], # up
    [0, 0, 0], # left
    [0, 0, 0], # right
    [0, 1, 2], # down right
    [0, 1, 2], # down left
    [0, -1, -2], # up right
    [0, -1, -2], # up left
]

dys = [
    [0, 0, 0], # down
    [0, 0, 0], # up
    [0, -1, -2], # left
    [0, 1, 2], # right
    [0, 1, 2], # down right
    [0, -1, -2], # down left
    [0, 1, 2], # up right
    [0, -1, -2], # up left
]

n, m = map(int, input().split())
arr = [
    list(input())
    for _ in range(n)
]

# check if x, y in range
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

ans = 0

for i in range(n):
    for j in range(m):
        x, y = i, j

        for direction in range(8):
            check_str = ''
            for dx, dy in zip(dxs[direction], dys[direction]):
                nx = x + dx
                ny = y + dy
                if not in_range(nx, ny):
                    break
                check_str += arr[nx][ny]

            if check_str == 'LEE':
                ans += 1

print(ans)