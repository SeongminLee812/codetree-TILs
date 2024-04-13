import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

INT_MIN = -sys.maxsize

dp = [
    [INT_MIN] * 4
    for _ in range(n + 1)
]

dp[0][0] = 0
dp[1][1] = arr[1]

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i][0] = dp[i - 2][0] + arr[i]
    for j in range(1, 4):
        dp[i][j] = max(dp[i - 1][j - 1] + arr[i], dp[i - 2][j] + arr[i])

print(max(dp[n]))