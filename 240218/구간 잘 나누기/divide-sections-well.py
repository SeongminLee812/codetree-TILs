import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

MAX_INT = 10000

def check(limit):
    now_sum = 0
    section = 1
    for i in range(n):
        if now_sum + arr[i] > limit:
            section += 1
            now_sum = 0
        now_sum += arr[i]


    if section <= m:
        return True
    return False


ans = sys.maxsize
for i in range(max(arr), MAX_INT + 1):
    if check(i):
        ans = min(ans, i)

print(ans)