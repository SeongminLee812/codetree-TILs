import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
w = [0] * (n + 1)
v = [0] * (n + 1)

for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())

dp = [
    [INT_MIN] * (m + 1)
    for _ in range(n + 1)
]

dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= w[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])

print(max(dp[n]))