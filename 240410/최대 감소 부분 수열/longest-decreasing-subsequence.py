import sys

n = int(input())

a = [sys.maxsize] + list(map(int, input().split()))

INT_MIN = -sys.maxsize

dp = [0] + [INT_MIN] * n

dp[0] = 0

for i in range(1, n + 1):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))