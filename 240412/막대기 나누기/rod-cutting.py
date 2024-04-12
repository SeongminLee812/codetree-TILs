n = int(input())

value = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = value[i]

for i in range(1, n + 1):
    best = 0
    for j in range(i):
        best = max(best, dp[i - j] + dp[j])
    dp[i] = best

print(dp[n])