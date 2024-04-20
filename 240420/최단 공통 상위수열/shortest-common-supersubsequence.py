s = input()
t = input()

dp = [
    [0] * len(t)
    for _ in range(len(s))
]

if s[0] == t[0]:
    dp[0][0] = 1
else:
    dp[0][0] = 2

for i in range(1, len(s)):
    if s[i] == t[0]:
        dp[i][0] = i
    else:
        dp[i][0] = dp[i - 1][0] + 1

for j in range(1, len(t)):
    if t[j] == s[0]:
        dp[0][j] = j
    else:
        dp[0][j] = dp[0][j - 1] + 1

for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

print(dp[len(s) - 1][len(t) - 1])