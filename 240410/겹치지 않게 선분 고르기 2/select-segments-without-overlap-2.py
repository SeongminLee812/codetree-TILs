n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [1] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if segments[j][0] > segments[i][1] or segments[i][0] > segments[j][1]:
            dp[i] += 1

print(max(dp))