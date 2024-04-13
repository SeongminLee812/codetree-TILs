import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

total_sum = sum(arr)
if total_sum % 2 != 0:
    print('No')
    sys.exit()

max_sum_of_group = total_sum // 2

dp = [
    [False] * (max_sum_of_group + 1)
    for _ in range(n + 1)
]

dp[0][0] = True

for i in range(1, n + 1):
    for j in range(max_sum_of_group + 1):
        if arr[i] <= j:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]
        else:
            dp[i][j] = dp[i - 1][j]

if dp[n][max_sum_of_group]:
    print('Yes')
else:
    print('No')