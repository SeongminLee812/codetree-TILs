import sys

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_overlapped(first_x1, first_y1, first_x2, first_y2,
                  second_x1, second_y1, second_x2, second_y2):
    board = [
        [0] * m
        for _ in range(n)
    ]

    for x in range(first_x1, first_x2 + 1):
        for y in range(first_y1, first_y2 + 1):
            board[x][y] += 1
    for x in range(second_x1, second_x2 + 1):
        for y in range(second_y1, second_y2 + 1):
            board[x][y] += 1

    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

def rec_sum(x1, y1, x2, y2):
    result = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            result += arr[x][y]
    return result

def find_max(first_x1, first_y1, first_x2, first_y2):
    result = -sys.maxsize

    first_rectangle = rec_sum(first_x1, first_y1, first_x2, first_y2)
    for second_x1 in range(n):
        for second_y1 in range(m):
            for second_x2 in range(second_x1, n):
                for second_y2 in range(second_y1, m):
                    if is_overlapped(first_x1, first_y1, first_x2, first_y2,
                                     second_x1, second_y1, second_x2, second_y2):
                        continue
                    second_rectangle = rec_sum(second_x1, second_y1, second_x2, second_y2)
                    if first_rectangle + second_rectangle > result:
                        result = first_rectangle + second_rectangle
    return result

ans = -sys.maxsize
for first_x1 in range(n):
    for first_y1 in range(m):
        for first_x2 in range(first_x1, n):
            for first_y2 in range(first_y1, m):
                ans = max(ans, find_max(first_x1, first_y1, first_x2, first_y2))

print(ans)