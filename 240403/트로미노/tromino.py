n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

blocks = [
    [[0, 1, 1], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 0]],
    [[0, 0, 1], [0, 1, 1]],
    [[0, 0, -1], [0, 1, 1]],
    [[0, 0, 0], [0, 1, 2]],
    [[0, 1, 2], [0, 0, 0]]
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

ans = 0

for x in range(n):
    for y in range(m):
        for block in blocks:
            value = 0
            for dx, dy in zip(block[0], block[1]):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    value = 0
                    break
                value += arr[nx][ny]
            ans = max(ans, value)

print(ans)