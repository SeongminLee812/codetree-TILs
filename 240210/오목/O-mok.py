from typing import *

def in_range(x, y):
    return x >= 0 and  x < 19 and y >= 0 and y < 19

def is_win(x, y):
    direction1 = [0, 0, 0, 0], [1, 2, 3, 4] # 오른쪽 가로 방향
    direction2 = [1, 2, 3, 4], [0, 0, 0, 0] # to downward
    direction3 = [1, 2, 3, 4], [1, 2, 3, 4] # to downward and rightward
    direction4 = [1, 2, 3, 4], [-1, -2, -3, -4] # to downward and left

    dr1_ok = True
    for dx, dy in zip(direction1[0], direction1[1]):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny) or a[x][y] != a[nx][ny]:
            dr1_ok = False
            break

    dr2_ok = True
    for dx, dy in zip(direction2[0], direction2[1]):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny) or a[x][y] != a[nx][ny]:
            dr2_ok = False
            break

    dr3_ok = True
    for dx, dy in zip(direction3[0], direction3[1]):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny) or a[x][y] != a[nx][ny]:
            dr3_ok = False
            break

    dr4_ok = True
    for dx, dy in zip(direction4[0], direction4[1]):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny) or a[x][y] != a[nx][ny]:
            dr4_ok = False
            break

    # print(f'dr1_ok={dr1_ok}, dr2_ok={dr2_ok}, dr3_ok={dr3_ok}')

    if dr1_ok:
        return x + 1, y + 2 + 1
    if dr2_ok:
        return x + 2 + 1, y + 1
    if dr3_ok:
        return x + 2 + 1, y + 2 + 1
    if dr4_ok:
        return x + 2 + 1, y - 2 + 1
    return False

a = [list(map(int, input().split())) for _ in range(19)]


for i in range(19):
    for j in range(19):
        if a[i][j] != 0:
            result = is_win(i, j)
            if result:
                print(a[i][j])
                print(' '.join(map(str, result)))