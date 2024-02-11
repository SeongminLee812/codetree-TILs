n, k = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

ans = -1

for i in range(n):
    if i == 0:
        prev_index = i
        continue
    now_index = i
    if now_index - prev_index <= k:
        ans = max(ans, bombs[i])
    prev_index = now_index

print(ans)