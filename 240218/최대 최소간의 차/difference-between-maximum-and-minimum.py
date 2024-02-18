import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

MIN_INT = min(arr)
MAX_INT = max(arr)

def cal_cost(min_limit, max_limit):
    cost = 0
    for i in range(n):
        if arr[i] < min_limit:
            cost += min_limit - arr[i]
        elif arr[i] > max_limit:
            cost += arr[i] - max_limit
    return cost

ans = sys.maxsize

for i in range(MIN_INT, MAX_INT - k + 1):
    min_limit = i
    max_limit = i + k
    cost = cal_cost(min_limit, max_limit)
    ans = min(ans, cost)

print(ans)