n, k = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

ans = -1

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if bombs[i] == bombs[j] and i - j <= k:
            ans = max(ans, bombs[i])

print(ans)