n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

dp = [
    [0] * (m + 1)
    for _ in range(n + 1)
]

for i in range(n + 1):
    dp[i][0] = 1


for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= arr[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - arr[i]])

    
if dp[n][m]:
    print('Yes')
else:
    print('No')