n = int(input())
h = [int(input()) for _ in range(n)]

ans = 0
for i in range(0, max(h) + 1):
    cnt = 0
    if h[0] > i:
        cnt += 1

    for j in range(1, n):
        if h[j - 1] <= i and h[j] > i:
            cnt += 1
    ans = max(ans, cnt)

print(ans)