import sys

n, h, t = map(int, input().split())

arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n - t + 1):
    cost = 0
    for j in range(i, i + t):
        now_cost = abs(arr[j] - h)
        cost += now_cost
    ans = min(ans, cost)

print(ans)