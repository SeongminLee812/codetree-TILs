n, m = map(int, input().split())

diamonds = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

diamonds = [(0, 0)] + diamonds

dp = [
    [-1] * (m + 1)
    for _ in range(n + 1)
]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= diamonds[i][0] and dp[i - 1][j - diamonds[i][0]] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - diamonds[i][0]] + diamonds[i][1])

print(max(dp[n]))