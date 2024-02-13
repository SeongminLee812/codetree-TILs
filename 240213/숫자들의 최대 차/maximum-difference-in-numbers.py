n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

c = list(set(arr))
c.sort()

ans = 0
for target in c:
    cnt = 0
    for elem in arr:
        if 0 <= elem - target <= k:
            cnt += 1
    ans = max(ans, cnt)

print(ans)