a = " " + input()
b = " " + input()

dp = [
    [[]] * len(b)
    for _ in range(len(a))
]


for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + [(i, j)]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

ans = [a[i] for i, j in dp[len(a) - 1][len(b) - 1]]
print(''.join(ans))