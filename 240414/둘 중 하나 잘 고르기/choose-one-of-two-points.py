import sys

INT_MIN = -sys.maxsize

n = int(input())

reds = [0] * (2 * n + 1)
blues = [0] * (2 * n + 1)

for i in range(1, 2 * n + 1):
    reds[i], blues[i] = map(int, input().split())

dp = [
    [INT_MIN] * (n + 1)
    for _ in range(2 * n + 1)
]

dp[0][0] = 0

for i in range(1, 2 * n + 1):
    dp[i][0] = dp[i - 1][0] + blues[i]
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + reds[i], dp[i - 1][j] + blues[i])


print(dp[2 * n][n])