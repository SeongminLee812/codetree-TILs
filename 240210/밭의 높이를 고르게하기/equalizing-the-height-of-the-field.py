import sys

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(0, n - t + 1):
    cost = 0
    for j in range(t):
        cost += abs(arr[i + j] - h)
    ans = min(cost, ans)

print(ans)