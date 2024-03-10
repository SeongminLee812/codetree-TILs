n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def print_filter():
    print('=' * 10)
    for line in filter:
        print(' '.join(map(str, line)))

def make_rectangle_length(x, y):
    # 현재 위치를 받아서 세로방향으로 먼저 직사각형을 만드는 함수
    if arr[x][y] < 0:
        return 0

    result = 0
    for col in range(m - y):
        cnt = 0
        is_pos_in_row = True

        # filter = [
        #     [0] * m
        #     for _ in range(n)
        # ]
        #
        # def print_filter():
        #     print('=' * 10)
        #     for line in filter:
        #         print(' '.join(map(str, line)))

        for row in range(n - x):
            for j in range(col + 1): # 직사각형의 가로변을 하나씩 늘리면서 검사
                nx, ny = x + row, y + j
                if arr[nx][ny] > 0:
                    cnt += 1
                    # filter[nx][ny] = 1
                else:
                    is_pos_in_row = False
                    break

            # 해당 행이 전부 양수가 아닌 경우 해당 행에서 개수를 셋던 것들 지워줌
            if not is_pos_in_row:
                cnt -= j
                break

        # if cnt > result:
        #     print_filter()
        #     print(cnt)

        result = max(cnt, result)

    return result

def make_rectangle_width(x, y):
    # 현재 위치를 받아서 가로방향으로 먼저 직사각형을 만드는 함수
    if arr[x][y] < 0:
        return 0

    result = 0
    for row in range(n - x):
        cnt = 0
        is_pos_in_row = True
        #
        # filter = [
        #     [0] * m
        #     for _ in range(n)
        # ]

        # def print_filter():
        #     print('=' * 10)
        #     for line in filter:
        #         print(' '.join(map(str, line)))

        for col in range(m - y):
            for j in range(row + 1): # 직사각형의 세로변을 하나씩 늘리면서 검사
                nx, ny = x + j, y + col
                if arr[nx][ny] > 0:
                    cnt += 1
                    # filter[nx][ny] = 1
                else:
                    is_pos_in_row = False
                    break

            # 해당 행이 전부 양수가 아닌 경우 해당 행에서 개수를 셋던 것들 지워줌
            if not is_pos_in_row:
                cnt -= j
                break

        # if cnt > result:
        #     print_filter()
        #     print(cnt)

        result = max(cnt, result)

    return result

ans = -1


for x in range(n):
    for y in range(m):
        cnt = 0
        cnt = make_rectangle_width(x, y)
        if cnt:
            ans = max(ans, cnt)
print(ans)