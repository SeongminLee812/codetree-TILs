# 맞출 수를 기준으로 완전탐색 -> 최소값을 target으로 두면서 target계속 올려가기
import sys

n, k = map(int, input().split())

arr = list(map(int, input().split()))

min_val, max_val = min(arr), max(arr)

def cost(target):
    value = 0
    for i in range(n):
        if arr[i] > target + k:
            value += arr[i] - (target + k)
        elif arr[i] < target:
                value += target - arr[i]
    return value

ans = sys.maxsize
for target in range(min_val, max_val + 1):
    curr_cost = cost(target)
    ans = min(ans, curr_cost)

print(ans)