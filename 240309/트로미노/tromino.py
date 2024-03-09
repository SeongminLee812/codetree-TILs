blocks = [
    [[0, 1, 1], [0, 0, 1]],
    [[0, 1, 0], [0, 0, 1]],
    [[0, 1, 1], [0, 0, -1]],
    [[0, 0, 1], [0, 1, 1]],
    [[0, 0, 0], [0, 1, 2]],
    [[0, 1, 2], [0, 0, 0]]
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
for x in range(n):
    for y in range(m):
        start_x, start_y = x, y
        for block in blocks:
            values = 0
            possible = True
            for dx, dy in zip(block[0], block[1]):
                nx, ny = start_x + dx, start_y + dy
                if not in_range(nx, ny):
                    possible = False
                    break
                values += arr[nx][ny]
            if not possible:
                continue
            ans = max(ans, values)

print(ans)