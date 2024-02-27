OFFSET = 1000
MAX_INT = OFFSET * 2 + 1
arr = [
    [0] * MAX_INT
    for _ in range(MAX_INT)
]

for i in range(2):
    if i == 0:
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 1
    else:
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 0

# 1인 ROW들 append한 후 min, max 구하고, 1인 col들 append한 후 min, max 구함..?
# row 구하기 -> sum이 1 이상이면 직사각형 있는 것임.
# col 구하기 -> (i == 0 and arr[i] = 1) or (arr[i - 1] == 0 and arr[i] == 1) == min_candi
#               min_col = min(min_candi, min_col)


row_candidate = []
col_candidate = []

for row in range(MAX_INT):
    for col in range(MAX_INT):
        if arr[row][col] != 0:
            row_candidate.append(row)
            col_candidate.append(col)

if row_candidate:
    answer = (max(row_candidate) - min(row_candidate) + 1) * (max(col_candidate) - min(col_candidate) + 1)
else:
    answer = 0
print(answer)