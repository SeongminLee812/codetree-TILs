import sys

n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

INT_MIN = -sys.maxsize
dp = [
    [INT_MIN] * (n + 1)
    for _ in range(n + 1)
]

dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if first[i] > second[j]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + second[j])
        elif first[i] == second[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
        else:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

ans = 0
for line in dp:
    ans = max(ans, max(line))
print(ans)