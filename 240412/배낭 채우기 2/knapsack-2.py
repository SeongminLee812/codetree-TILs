n, m = map(int, input().split())

value = [0] * (n + 1)
weight = [0] * (n + 1)

for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

dp = [0] * (m + 1)

for i in range(1, m + 1):
    for j in range(n + 1):
        if i >= weight[j]:
            dp[i] = max(dp[i], dp[i - weight[j]] + value[j])

print(dp[m])