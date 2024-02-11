n, b = map(int, input().split())

p = [int(input()) for _ in range(n)]
p.sort()

# search max value
ans = 0

for i in range(n):
    # initialize
    p[i] = p[i] // 2
    cnt = 0
    money = b
    for j in range(n):
        cnt += 1
        money -= p[j]
        if money < 0:
            cnt -= 1
            break
    p[i] = p[i] * 2
    ans = max(ans, cnt)

print(ans)