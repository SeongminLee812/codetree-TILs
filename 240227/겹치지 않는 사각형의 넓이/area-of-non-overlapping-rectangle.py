OFFSET = 1000
MAX_INT = 2 * OFFSET + 1

arr = [
    [0] * MAX_INT
    for _ in range(MAX_INT)
]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

x1, y1, x2, y2 = map(int, input().split())
for x in range(x1, x2):
    for y in range(y1, y2):
        arr[x][y] = 0

answer = 0
for row in arr:
    answer += sum(row)
print(answer)