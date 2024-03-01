n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

ans = 0

for start in range(1, n + 1):
    total = 0
    now = start
    cnt = 0
    while cnt < m:
        total += arr[now]
        now = arr[now]
        cnt += 1
    ans = max(ans, total)

print(ans)