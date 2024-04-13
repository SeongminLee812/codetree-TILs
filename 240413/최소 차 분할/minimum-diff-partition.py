n = int(input())

arr = [0] + list(map(int, input().split()))

total_sum = sum(arr)
max_sum_of_group = total_sum // 2

dp = [False] * (max_sum_of_group + 1)

dp[0] = True

for i in range(n + 1):
    for j in range(max_sum_of_group + 1):
        if arr[i] <= j and dp[j - arr[i]]:
            dp[j] = True



sum_a = 0
for i in range(max_sum_of_group + 1):
    if dp[i]:
        sum_a = max(sum_a, i)

ans = abs(total_sum - (2 * sum_a))
print(ans)