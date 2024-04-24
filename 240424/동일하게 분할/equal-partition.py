import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

if sum(arr) % 2 != 0:
    print('No')
    sys.exit()

target = sum(arr) // 2

dp = [
    [False] * (target + 1)
    for _ in range(n + 1)
]

dp[0][0] = True

for i in range(1, n + 1):
    for j in range(target + 1):
        dp[i][j] = dp[i - 1][j]
        if arr[i] <= j:
            dp[i][j] = any([dp[i][j], dp[i - 1][j - arr[i]]])

if dp[n][target]:
    print('Yes')
else:
    print('No')