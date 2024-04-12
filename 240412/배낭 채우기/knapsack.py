n, m = map(int, input().split())

weight = [0] * (n + 1)
value = [0] * (n + 1)

for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

dp = [-1] * (m + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(m, 0, -1):
        if weight[i] <= j:
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
        else:
            dp[j] = dp[j]

print(max(dp))