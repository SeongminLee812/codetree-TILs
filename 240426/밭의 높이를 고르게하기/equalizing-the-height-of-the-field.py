import sys

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize
if n == 1:
    print(abs(h - arr[0]))
    sys.exit()
    
for i in range(n - t):
    diff = 0
    for j in range(i, i + t):
        diff += abs(arr[j] - h)
    ans = min(diff, ans)

print(ans)