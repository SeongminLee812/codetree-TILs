n, k = map(int, input().split())

placed = [0] * 100
for _ in range(n):
    candies, spot = map(int, input().split())
    placed[spot] += candies
ans = 0

if k >= 50:
    ans = sum(placed)
else:
    for c in range(k, 100 - k):
        value = sum(placed[c - k:c]) + sum(placed[c:c + k + 1])
        # print(f'c={c}, value={value}')
        # print(f'placed = {placed[c - k:c]} + {placed[c:c + k + 1]}')
        ans = max(ans, value)

print(ans)