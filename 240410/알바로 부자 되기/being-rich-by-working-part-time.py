n = int(input())
alba = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
alba = [(0, 0, 0)] + alba

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if alba[j][1] < alba[i][0]:
            dp[i] = max(dp[i], dp[j] + alba[i][2])

print(max(dp))