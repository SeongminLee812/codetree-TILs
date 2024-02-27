OFFSET = 100
MAX_INT = 2 * OFFSET + 1

arr = [
    [0] * MAX_INT
    for _ in range(MAX_INT)
]

n = int(input())

for _ in range(n):
    x0, y0 = map(int, input().split())
    for x in range(x0, x0 + 8):
        for y in range(y0, y0 + 8):
            arr[x][y] = 1

answer = 0
for row in arr:
    answer += sum(row)

print(answer)