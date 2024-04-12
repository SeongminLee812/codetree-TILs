n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (m + 1)
dp[0] = 1

for j in range(n):
    for i in range(m, 0, -1):
        if i >= arr[j]:
            dp[i] = max(dp[i], dp[i - arr[j]])

if dp[m]:
    print('Yes')
else:
    print('No')