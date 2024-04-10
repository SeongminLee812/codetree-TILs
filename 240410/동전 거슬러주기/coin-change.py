n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [10001] * (m + 1)
for j in range(n):
    dp[coins[j]] = 1

for i in range(m + 1):
    for j in range(n):
        if coins[j] < i and dp[i - coins[j]] != -1:
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])