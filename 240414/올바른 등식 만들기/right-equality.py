import sys

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

INT_MIN = -sys.maxsize

dp = [
    [0] * 41
    for _ in range(n + 2)
]

dp[2][20 - arr[1]] = 1
dp[2][20 + arr[1]] = 1


# 뿌리는 dp로 접근
for i in range(2, n + 1):
    for j in range(41):
        if 0 <= j - arr[i] <= 40:
            dp[i + 1][j - arr[i]] += dp[i][j]
        if 0 <= j + arr[i] <= 40:
            dp[i + 1][j + arr[i]] += dp[i][j]


print(dp[n + 1][m + 20])