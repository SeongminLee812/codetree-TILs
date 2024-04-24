import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

if sum(arr) % 2 != 0:
    print('No')
    sys.exit()

target = sum(arr) // 2

dp = [False] * (target + 1)

dp[0] = True

for j in range(n + 1):
    for i in range(target, -1, -1):
        if i >= arr[j]:
            dp[i] = any([dp[i], dp[i - arr[j]]])

if dp[target]:
    print('Yes')
else:
    print('No')