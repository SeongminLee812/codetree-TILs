OFFSET = 100
MAX_INT = OFFSET * 2 + 1
arr = [
    [0] * MAX_INT
    for _ in range(MAX_INT)
]

n = int(input())
for i in range(n):
    # red rectangle
    if i % 2 == 0:
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 0

    # blue rectangle
    else:
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 1


answer = 0
for row in arr:
    answer += sum(row)
print(answer)