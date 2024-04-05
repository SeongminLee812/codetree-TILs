n = int(input())

dp = [0] * 1001

dp[0] = 1
dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3)
    for j in range(3, i + 1):
        dp[i] += dp[i - j] * 2
    dp[i] %= 1000000007

print(dp[n])