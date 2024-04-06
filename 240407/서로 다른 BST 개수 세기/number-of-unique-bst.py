n = int(input())

dp = [0] * 20

dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    for j in range(0, i):
        left_tree = j
        right_tree = i - j - 1
        dp[i] += dp[left_tree] * dp[right_tree]


print(dp[n])