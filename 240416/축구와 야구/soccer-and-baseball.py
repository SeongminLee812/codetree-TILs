import sys

n = int(input())

INT_MIN = -sys.maxsize

s = [0] * (n + 1)
b = [0] * (n + 1)

for i in range(1, n + 1):
    s[i], b[i] = map(int, input().split())
dp = [
        [
            [INT_MIN] * 10
            for _ in range(12)
      ]
    for _ in range(n + 1)]

dp[0][0][0] = 0

for i in range(1, n + 1):
    dp[i][0][0] = 0
    for j in range(12):
        for k in range(10):
            if j == 0 and k == 0:
                continue
            if j == 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + b[i], dp[i - 1][j][k])
            elif k == 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + s[i], dp[i - 1][j][k])
            else:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + s[i], dp[i - 1][j][k - 1] + b[i], dp[i - 1][j][k])

print(dp[n][11][9])