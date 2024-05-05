import sys

n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

# 사각형 하나 탐색하기
def get_rectangle_sum(start_x, start_y, range_horizontal, range_vertical):
    x, y = start_x, start_y
    n, m = range_horizontal, range_vertical
    result = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if not in_range(x + i, y + j):
                break
            result += arr[x + i][y + j]

    return result

ans = -sys.maxsize
for x in range(n):
    for y in range(m):
        for i in range(n - x):
            for j in range(m - y):
                first_rectangle = get_rectangle_sum(x, y, i, j)

                # 여기서부터 두번째 사각형 돌리기
                for second_x in range(n):
                    for second_y in range(m):
                        # 첫번째 사각형 안에 들어오는 경우 제외
                        if second_x <= x + i and second_y <= y + j:
                            continue
                        for k in range(n - second_x):
                            for l in range(m - second_y):
                                second_rectangle = get_rectangle_sum(second_x, second_y, k, l)

                                ans = max(ans, first_rectangle + second_rectangle)

print(ans)