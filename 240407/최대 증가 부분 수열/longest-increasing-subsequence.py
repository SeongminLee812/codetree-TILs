import sys

n = int(input())

a = [0] + list(map(int, input().split()))
INT_MIN = -sys.maxsize
MAX_VAL = max(a)
dp = [
    [INT_MIN] * (MAX_VAL + 1)
    for _ in range(len(a))
]

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(MAX_VAL + 1):
        dp[i][j] = dp[i - 1][j]
        if a[i] == j:
            for l in range(j):
                if dp[i - 1][l] != INT_MIN:
                    dp[i][j] = max(dp[i][j], dp[i - 1][l] + 1)

print(max(dp[n]))