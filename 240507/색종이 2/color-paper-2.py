n = int(input())

arr = [
    [False] * 502
    for _ in range(502)
]

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = x1 + 1, y1 + 1
    for x in range(x1, x1 + 10):
        for y in range(y1, y1 + 10):
            arr[x][y] = True

ans = 0
for x in range(501):
    for y in range(501):
        if arr[x][y] != arr[x + 1][y]:
            ans +=1
        if arr[x][y] != arr[x][y + 1]:
            ans += 1

print(ans)