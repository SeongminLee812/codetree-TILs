x, y = map(int, input().split())

ans = 0
for i in range(x, y + 1):
    value = i // 10000 + i // 1000 % 10 + i // 100 % 10 + i // 10 % 10 + i % 10
    ans = max(ans, value)

print(ans)