import sys

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

ans = sys.maxsize

for i in range(n):
    diff = arr[i + n] - arr[i]
    ans = min(diff, ans)

print(ans)