n = int(input())

MOD = 10e9 + 7

dp = [
    [0] * 3
    for _ in range(n + 1)
]

dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(3):
        dp[i][j] += dp[i - 1][j] * 2
        if j >= 1:
            dp[i][j] += dp[i - 1][j - 1]
        if i - j > 2 and dp[i][j] > 0:
            dp[i][j] -= 1
        dp[i][j] = int(dp[i][j] % MOD)

print(sum(dp[n]))