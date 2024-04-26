import sys

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))



ans = -sys.maxsize
for i in range(1, n + 1):
    index = i
    total = 0
    for _ in range(m):
        total += arr[index]
        index = arr[index]
    ans = max(ans, total)

print(ans)