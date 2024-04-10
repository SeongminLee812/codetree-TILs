n = int(input())

dp = [0] * 10001

dp[0] = 1

for i in range(1, n + 1):
    for j in [1, 2, 5]:
        if i >= j:
            dp[i] += dp[i - j]
            dp[i] %= 10007


print(dp[n])