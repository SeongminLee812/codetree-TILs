n, m = map(int, input().split())

arr = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def is_comfortable(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        return True
    return False

result = []

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1

    arr[r][c] = 1
    if is_comfortable(r, c):
        result.append('1')
    else:
        result.append('0')

print('\n'.join(result))