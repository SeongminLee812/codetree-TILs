n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

dp = [
    [0] * 41
    for _ in range(n + 2)
]

dp[0][20] = 1

# 가져오는 dp로 작성
for i in range(1, n + 1):
    for j in range(41):
        if j - arr[i] >= 0:
            dp[i][j] += dp[i - 1][j - arr[i]]
        if j + arr[i] <= 40:
            dp[i][j] += dp[i - 1][j + arr[i]]

print(dp[n][m + 20])