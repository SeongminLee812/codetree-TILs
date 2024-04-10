n, m = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0] * n
    for _ in range(n)
]

dp[0][0] = 1

for i in range(1, n):
    for j in range(1, m):
        for k in range(i):
            for l in range(j):
                if dp[k][l] == 0:
                    continue
                if a[k][l] < a[i][j]:
                    dp[i][j] = max(dp[i][j], dp[k][l] + 1)

ans = 0
for line in dp:
    ans = max(ans, max(line))

print(ans)