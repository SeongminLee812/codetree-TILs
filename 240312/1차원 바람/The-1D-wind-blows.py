n, m, q = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def wind_from_left(row: int):
    temp = arr[row][m - 1]
    for i in range(m - 1, 0, -1):
        arr[row][i] = arr[row][i - 1]
    arr[row][0] = temp


def wind_from_right(row: int):
    temp = arr[row][0]
    for i in range(0, m - 1):
        arr[row][i] = arr[row][i + 1]
    arr[row][m - 1] = temp

def has_same(row1: int, row2: int):
    for i in range(m):
        if arr[row1][i] == arr[row2][i]:
            return True
    return False

def in_range(row):
    return row >= 0 and row < n

def go(row: int, d):
    global already_pushed
    already_pushed[row] = True
    if not in_range(row):
        return


    if d == 'L':
        wind_from_left(row)

        if in_range(row - 1) and has_same(row, row - 1) and not already_pushed[row - 1]:
            go(row - 1, 'R')
        if in_range(row + 1) and has_same(row, row + 1) and not already_pushed[row + 1]:
            go(row + 1, 'R')

    else:
        wind_from_right(row)
        # print(f'go #{row}')
        # for line in arr:
        #     print(' '.join(map(str, line)))

        if in_range(row - 1) and has_same(row, row - 1) and not already_pushed[row - 1]:
            go(row - 1, 'L')
        if in_range(row + 1) and has_same(row, row + 1) and not already_pushed[row + 1]:
            go(row + 1, 'L')



for _ in range(q):
    row, direction = input().split()
    row = int(row) - 1

    # initialized already pushed table
    already_pushed = [False] * n
    go(row, direction)

for line in arr:
    print(' '.join(map(str, line)))