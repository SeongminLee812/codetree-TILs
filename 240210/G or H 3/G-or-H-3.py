n, k = map(int, input().split())

placed = [0] * 10001
length = 0

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'G':
        placed[a] = 1
    elif b == 'H':
        placed[a] = 2
    length = max(length, a)

placed = placed[:length + 1]

ans = 0
for i in range(length - k + 1):
    val = 0
    for j in range(i, i + k + 1):
        val += placed[j]
    ans = max(ans, val)

print(ans)