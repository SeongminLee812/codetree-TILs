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
    [-1] * n
    for _ in range(n)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def find_max(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    best = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] < arr[x][y]:
            best = max(best, find_max(nx, ny) + 1)

    dp[x][y] = best
    return dp[x][y]

for i in range(n):
    for j in range(n):
        dp[i][j] = find_max(i, j)

ans = 0
for line in dp:
    ans = max(ans, max(line))

print(ans)