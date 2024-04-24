import sys
INT_MIN = -sys.maxsize

a = " " + input()
b = " " + input()

dp = [
    [INT_MIN] * len(b)
    for _ in range(len(a))
]

for i in range(len(a)):
    dp[i][0] = i
for j in range(len(b)):
    dp[0][j] = j

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

print(dp[len(a) - 1][len(b) - 1])