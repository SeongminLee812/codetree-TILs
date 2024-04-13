import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

total_sum = sum(arr)
if total_sum % 2 != 0:
    print('No')
    sys.exit()

max_sum_of_group = total_sum // 2

dp = [False] * (max_sum_of_group + 1)

dp[0] = True

for i in range(n):
    for j in range(max_sum_of_group, 0, -1):
        if arr[i] <= j:
            dp[j] = dp[j - arr[i]]

if dp[max_sum_of_group]:
    print('Yes')
else:
    print('No')