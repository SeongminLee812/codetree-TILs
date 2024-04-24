import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
w = [0] * (n + 1)
v = [0] * (n + 1)

for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())

dp = [INT_MIN] * (m + 1)
dp[0] = 0

for j in range(n + 1):
    for i in range(m, -1, -1):
        if w[j] <= i:
            dp[i] = max(dp[i], dp[i - w[j]] + v[j])

print(max(dp))