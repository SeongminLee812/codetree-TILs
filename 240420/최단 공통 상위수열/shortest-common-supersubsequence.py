s = " " + input()
t = " " + input()

dp = [
    [0] * len(t)
    for _ in range(len(s))
]


for i in range(len(s)):
    dp[i][0] = i
for j in range(len(t)):
    dp[0][j] = j


for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1


print(dp[len(s) - 1][len(t) - 1])