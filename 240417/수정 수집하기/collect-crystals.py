import sys
INT_MIN = -sys.maxsize

n, max_move = map(int, input().split())

arr = [
    [0, 0]
    for _ in range(n + 1)
]

crystal = input()

for i, c in enumerate(crystal, start=1):
    if c == 'L':
        arr[i][0] = 1
    else:
        arr[i][1] = 1

dp = [
    [
        [INT_MIN] * (max_move + 1)
        for _ in range(2)
    ] for _ in range(n + 1)
]

dp[0][0][0] = 0

for i in range(1, n + 1):
    for j in range(2):
        for k in range(max_move + 1):
            if k >= 1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + arr[i][j], dp[i - 1][1 - j][k - 1] + arr[i][j])
            else:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + arr[i][j])

ans = 0
for j in range(2):
    ans = max(ans, max(dp[n][j]))

print(ans)