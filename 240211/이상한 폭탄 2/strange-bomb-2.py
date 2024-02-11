n, k = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

ans = -1

for i in range(n - 1):
    for j in range(i + 1, n):
        if j - i > k:
            continue
        if bombs[i] != bombs[j]:
            continue
        ans = max(ans, bombs[i])

print(ans)