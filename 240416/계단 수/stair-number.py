n = int(input())
MOD = 1e9 + 7

dp = [
    [0] * 10
    for _ in range(n + 1)
]

# initialize
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(0, 10):
        if j == 9:
            dp[i][j] = (dp[i - 1][j - 1]) % MOD
        elif j == 0:
            dp[i][j] = (dp[i - 1][j + 1]) % MOD
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

print(int(sum(dp[n]) % MOD))