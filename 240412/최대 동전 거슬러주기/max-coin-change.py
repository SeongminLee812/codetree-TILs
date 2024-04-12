n, m = map(int, input().split())

coins = list(map(int, input().split()))

INT_MAX = 10001
dp = [-1] * INT_MAX

dp[0] = 0

for i in range(1, m + 1):
    for j in range(n):
        if i >= coins[j] and dp[i - coins[j]] != -1:
            dp[i] = max(dp[i], dp[i - coins[j]] + 1)

print(dp[m])