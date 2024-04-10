n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

segments.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if segments[j][1] < segments[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))