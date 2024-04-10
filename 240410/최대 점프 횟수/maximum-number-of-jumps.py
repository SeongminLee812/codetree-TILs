n = int(input())

a = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    for j in range(i):
        if a[j] + j >= i:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] == 0:
        break

print(max(dp))