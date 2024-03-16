arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

direction = input()

def push(direction):
    if direction == 'L':
        for row in range(0, 4):
            temp_array = [0] * 4
            temp_idx = 0
            for col in range(4):
                if arr[row][col]:
                    temp_array[temp_idx] = arr[row][col]
                    temp_idx += 1
            arr[row] = temp_array

    elif direction == 'R':
        for row in range(4):
            temp_array = [0] * 4
            temp_idx = 3 # 가장 뒤부터 시작
            for col in range(3, -1, -1):
                if arr[row][col]:
                    temp_array[temp_idx] = arr[row][col]
                    temp_idx -= 1
            arr[row] = temp_array

    elif direction == 'U':
        for col in range(4):
            temp_array = [0] * 4
            temp_idx = 0
            for row in range(4):
                if arr[row][col]:
                    temp_array[temp_idx] = arr[row][col]
                    temp_idx += 1
            for replace_row in range(4):
                arr[replace_row][col] = temp_array[replace_row]

    else:
        for col in range(4):
            temp_array = [0] * 4
            temp_idx = 3
            for row in range(3, -1, -1):
                if arr[row][col]:
                        temp_array[temp_idx] = arr[row][col]
                        temp_idx -= 1
            for replace_row in range(4):
                arr[replace_row][col] = temp_array[replace_row]

def fuse(direction):
    if direction == 'L':
        for row in range(0, 4):
            col_idx = 0
            while col_idx < 3:
                if arr[row][col_idx] == arr[row][col_idx + 1]:
                    arr[row][col_idx] = arr[row][col_idx] + arr[row][col_idx + 1]
                    arr[row][col_idx + 1] = 0
                    col_idx += 2
                else:
                    col_idx += 1

    elif direction == 'R':
        for row in range(0, 4):
            col_idx = 3
            while col_idx > 0:
                if arr[row][col_idx] == arr[row][col_idx - 1]:
                    arr[row][col_idx] = arr[row][col_idx] + arr[row][col_idx - 1]
                    arr[row][col_idx - 1] = 0
                    col_idx -= 2
                else:
                    col_idx -= 1


    elif direction == 'U':
        for col in range(4):
            row_idx = 0
            while row_idx < 3:
                if arr[row_idx][col] == arr[row_idx + 1][col]:
                    arr[row_idx][col] = arr[row_idx][col] + arr[row_idx + 1][col]
                    arr[row_idx + 1][col] = 0
                    row_idx += 2
                else:
                    row_idx += 1

    else:
        for col in range(4):
            row_idx = 3
            while row_idx > 0:
                if arr[row_idx][col] == arr[row_idx - 1][col]:
                    arr[row_idx][col] = arr[row_idx][col] + arr[row_idx - 1][col]
                    arr[row_idx - 1][col] = 0
                    row_idx -= 2
                else:
                    row_idx -= 1


push(direction=direction)
fuse(direction=direction)
push(direction=direction)
for line in arr:
    print(' '.join(map(str, line)))