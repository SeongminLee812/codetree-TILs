# 아무거나 2개를 잘 골라서 total에서 빼고, 그 차이가 최소가 되도록
import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr)
ans = sys.maxsize

for i in range(n - 1):
    for j in range(i + 1, n):
        value = total - arr[i] - arr[j]
        diff = abs(s - value)
        ans = min(diff, ans)

print(ans)