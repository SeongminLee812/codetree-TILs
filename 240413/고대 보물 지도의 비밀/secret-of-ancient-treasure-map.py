import sys

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

INT_MIN = -sys.maxsize

dp = [
    [INT_MIN] * (k + 2)
    for _ in range(n + 2)
]

dp[0][0] = 0
# if arr[1] < 0:
#     dp[1][1] = arr[1]
#     dp[1][0] = 0
# else:
#     dp[1][0] = arr[1]

for i in range(n + 1):
    if arr[i] < 0:
        for j in range(k + 1):
            if dp[i][j] == INT_MIN:
                continue
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + arr[i])
    else:
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + arr[i], arr[i])
        for j in range(k + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + arr[i])


ans = INT_MIN

for line in dp:
    ans = max(ans, max(line))

print(ans)