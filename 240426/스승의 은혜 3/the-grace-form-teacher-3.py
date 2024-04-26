n, b = map(int, input().split())

p = [0] * n
s = [0] * n
for i in range(n):
    p[i], s[i] = map(int, input().split())

ans = 0
for i in range(n):
    p[i] //= 2
    candidate = []
    for j in range(n):
        candidate.append(p[j] + s[j])
    candidate.sort()
    remain = b
    k = 0
    while remain and k < n:
        remain -= candidate[k]
        if remain < 0:
            break
        k += 1
    ans = max(ans, k)

    p[i] *= 2

print(ans)