import sys
INT_MIN = -sys.maxsize

MOD = 1e9 + 7

n = int(input())

dp = [
    [
        [0] * 4
        for _ in range(4)
    ] for _ in range(n + 1)
]

dp[0][0][0] = 1
dp[0][1][0] = 1
dp[0][0][1] = 1

for i in range(n):
    for j in range(3):
        for k in range(3):
            # G받는 경우
            dp[i + 1][0][k] = (dp[i + 1][0][k] + dp[i][j][k]) % MOD
            # B 받는 경우
            dp[i + 1][j + 1][k] = (dp[i + 1][j + 1][k] + dp[i][j][k]) % MOD
            # T받는 경우
            dp[i + 1][0][k + 1] = (dp[i + 1][0][k + 1] + dp[i][j][k]) % MOD

ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n - 1][j][k]) % MOD
print(int(ans % MOD))