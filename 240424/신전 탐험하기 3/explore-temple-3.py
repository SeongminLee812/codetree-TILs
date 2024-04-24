import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())

stair = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [INT_MIN] * m
    for _ in range(n)
]

for j in range(m):
    dp[0][j] = stair[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + stair[i][j])

print(max(dp[n - 1]))