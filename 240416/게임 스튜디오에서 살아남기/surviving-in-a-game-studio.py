n = int(input())

MOD = 1e9 + 7

dp = [
        [
            [0] * 4
            for _ in range(4)
        ] for _ in range(n + 1)
    ]

dp[1][0][0] = 1
dp[1][0][1] = 1
dp[1][1][0] = 1

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) % MOD # G가 붙는 경우
            dp[i + 1][j][k + 1] = (dp[i + 1][j][k + 1] + dp[i][j][k]) % MOD # B가 붙는 경우
            dp[i + 1][j + 1][0] = (dp[i + 1][j + 1][0] + dp[i][j][k]) % MOD # T가 붙는 경우


ans = 0

for j in range(3):
    for k in range(3):
        ans = (ans + dp[n][j][k]) % MOD
print(int(ans % MOD))