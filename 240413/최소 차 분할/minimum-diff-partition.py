n = int(input())

arr = [0] + list(map(int, input().split()))

total_sum = sum(arr)
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

sum_a = 0
for i in range(n + 1):
    for j in range(max_sum_of_group + 1):
        if dp[i][j]:
            sum_a = max(sum_a, j)
# print(sum_a)
# 
# for j in range(max_sum_of_group + 1):
#     print(j, end='\t')
# print()
# for i in range(n + 1):
#     for j in range(max_sum_of_group + 1):
#         print(dp[i][j], end='\t')
#     print()

ans = abs(total_sum - (2 * sum_a))
print(ans)