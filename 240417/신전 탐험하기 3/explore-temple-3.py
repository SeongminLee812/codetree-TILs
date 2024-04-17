n, m = map(int, input().split())

arr = [[0] * m]

for _ in range(1, n + 1):
    floor = list(map(int, input().split()))
    arr.append(floor)

dp = [
    [0] * (m)
    for _ in range(n + 1)
]

for j in range(m):
    dp[1][j] = arr[1][j]

for i in range(2, n + 1):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + arr[i][j])


print(max(dp[n]))