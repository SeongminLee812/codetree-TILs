import sys

n = int(input())
INT_MIN = -sys.maxsize

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr = [[0, 0, 0]] + arr

dp = [
    [
        [0] * 3
        for _ in range(n + 1)
    ] for _ in range(3)
]

for h in range(3):
    for j in range(3):
        if j == h:
            dp[h][1][j] = arr[1][j]
        else:
            dp[h][1][j] = INT_MIN

    for i in range(2, n):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[h][i][j] = max(dp[h][i][j], dp[h][i - 1][k] + arr[i][j])

# 마지막 층
for h in range(3):
    for j in range(3):
        for k in range(3):
            if h != j and k != j:
                dp[h][n][j] = max(dp[h][n][j], dp[h][n - 1][k] + arr[n][j])

ans = 0
for h in range(3):
    ans = max(ans, max(dp[h][n]))
print(ans)