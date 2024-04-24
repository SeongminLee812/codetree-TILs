import sys
INT_MIN = -sys.maxsize

n = int(input())

s = [0] * (n + 1)
b = [0] * (n + 1)

for i in range(1, n + 1):
    s[i], b[i] = map(int, input().split())

dp = [
    [
        [INT_MIN] * 10 # 야구 팀 수
        for _ in range(12) # 축구 선수 수
    ] for _ in range(n + 1) # 전체 학생 수
]

dp[0][0][0] = 0
for i in range(1, n + 1):
    for j in range(12):
        for k in range(10):
            dp[i][j][k] = dp[i - 1][j][k]
            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + s[i], dp[i - 1][j][k - 1] + b[i])

print(dp[n][11][9])