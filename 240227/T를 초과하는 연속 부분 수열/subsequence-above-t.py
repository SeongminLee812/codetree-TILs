n, t = map(int, input().split())

arr = list(map(int, input().split()))

ans = 1
cnt = 1

for i in range(n):
    if i == 0:
        continue
    if arr[i - 1] > t and arr[i] > t:
        cnt += 1
    if arr[i] <= t or i == n - 1:
        ans = max(ans, cnt)
        cnt = 1
print(ans)