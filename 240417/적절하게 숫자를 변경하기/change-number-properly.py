n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

numbers = [
    [0] * 5
    for _ in range(n + 1)
]

for index, num in enumerate(arr):
    if num == 0:
        continue
    numbers[index][num] = 1

dp = [
    [
        [0] * (m + 1)
        for _ in range(5)
    ]
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    for j in range(1, 5):
        for k in range(m + 1):
            # k == 0인경우 현재 위치 고집
            if k == 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + numbers[i][j])

            else:
                # 이동하지 않는 경우
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + numbers[i][j])
                # 이동하는 경우
                for h in range(1, 5):
                    if h == j:
                        continue
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][h][k - 1] + numbers[i][j])

ans = 0
for index in dp[n]:
    ans = max(ans, max(index))

print(ans)