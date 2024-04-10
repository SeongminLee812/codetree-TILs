n, m = map(int, input().split())
arr = list(map(int, input().split()))

INT_MAX = 10001
dp = [INT_MAX] * 10001
dp[0] = 0

for j in range(n):
    for i in range(m + 1, -1, -1):
        if i >= arr[j]:
            dp[i] = min(dp[i], dp[i - arr[j]] + 1)


if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])