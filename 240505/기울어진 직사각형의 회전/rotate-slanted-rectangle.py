n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c, m1, m2, m3, m4, dir_num = map(int, input().split())
r, c = r - 1, c - 1

def extract_element_pos(start_x, start_y, m1, m2):
    result_list = []

    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    x, y = start_x, start_y

    for dx, dy, steps in zip(dxs, dys, [m1, m2, m1, m2]):
        for _ in range(steps):
            nx, ny = x + dx, y + dy
            result_list.append((nx, ny))
            x, y = nx, ny

    return result_list

def rotate(start_x, start_y, m1, m2, dir_num):
    # dir_num은 오직 회전에만 기여하는 파라미터
    pos_list = extract_element_pos(start_x, start_y, m1, m2)
    elem_list = [arr[x][y] for x, y in pos_list]
    n = len(elem_list)

    if dir_num == 0:
        temp = elem_list[-1]
        for i in range(n - 1, 0, -1):
            elem_list[i] = elem_list[i - 1]
        elem_list[0] = temp
    if dir_num == 1:
        temp = elem_list[0]
        for i in range(n - 1):
            elem_list[i] = elem_list[i + 1]
        elem_list[-1] = temp

    for i, (x, y) in enumerate(pos_list):
        arr[x][y] = elem_list[i]

rotate(r, c, m1, m2, dir_num)

for line in arr:
    print(' '.join(map(str, line)))