n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

q = []
for i in range(n):
    for j in range(n):
        q.append((arr[i][j], i, j))
q.sort()

dp = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, t):
    if not in_range(x, y):
        return False
    if arr[x][y] >= t:
        return False
    return True


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for value, x, y in q:
    max_val = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, arr[x][y]):
            max_val = max(max_val, dp[nx][ny])
    dp[x][y] = max_val + 1

ans = 0
for line in dp:
    ans = max(ans, max(line))

print(ans)