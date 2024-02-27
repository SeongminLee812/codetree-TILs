OFFSET = 100

n = int(input())

arr = [
    [0] * (OFFSET * 2 + 1)
    for _ in range(OFFSET * 2 + 1)
]

for _ in range(n):

    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

answer = 0
for row in arr:
    answer += sum(row)
print(answer)