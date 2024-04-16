import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())

start = [0] * (n + 1)
end = [0] * (n + 1)
value = [0] * (n + 1)

for i in range(1, n + 1):
    start[i], end[i], value[i] = map(int, input().split())


dp = [
    [INT_MIN] * (n + 1)
    for _ in range(m + 1)
]
dp[1] = [0] * (n + 1)

for i in range(2, m + 1):
    for j in range(1, n + 1):
        if start[j] <= i <= end[j]: # 옷을 입을 수 있는 상태인지 확인
            dp[i][j] = 0
            for k in range(1, n + 1):
                if start[k] <= i - 1 <= end[k]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(value[j] - value[k]))

print(max(dp[m]))