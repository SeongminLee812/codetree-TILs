n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr = [[0, 0, 0]] + arr

dp = [
    [0] * 3
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if k == j:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + arr[i][j])

print(max(dp[n]))