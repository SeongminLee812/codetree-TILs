OFF_SET = 100

n = int(input())

arr = [
    [0] * (2 * OFF_SET + 1)
    for _ in range(2 * OFF_SET + 1)
]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFF_SET, y1 + OFF_SET, x2 + OFF_SET, y2 + OFF_SET
    if i % 2 == 0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = -1
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 1

ans = 0
for i in range(2 * OFF_SET + 1):
    for j in range(2 * OFF_SET + 1):
        if arr[i][j] == 1:
            ans += 1

print(ans)