a = [list(map(int, list(input()))) for _ in range(3)]

def in_range(x, y):
    return x >= 0 and x < 3 and y >= 0 and y < 3

def can_go(x, y, targets):
    if not in_range(x, y):
        return False
    if a[x][y] not in targets:
        return False
    return True

def check(compo1, compo2):
    targets = [compo1, compo2]
    dxs = [1, 0, 1]
    dys = [0, 1, 1]

    for i in range(3):
        for j in range(3):
            if a[i][j] in targets:
                for dx, dy in zip(dxs, dys):
                    compo1_cnt = 0
                    compo2_cnt = 0

                    if a[i][j] == compo1:
                        compo1_cnt += 1
                    elif a[i][j] == compo2:
                        compo2_cnt += 1

                    move = 1
                    nx = i + dx
                    ny = j + dy
                    while can_go(nx, ny, targets):
                        if a[nx][ny] == compo1:
                            compo1_cnt += 1
                        elif a[nx][ny] == compo2:
                            compo2_cnt += 1

                        move += 1
                        x = nx
                        y = ny
                        nx, ny = x + dx, y + dy

                    if move == 3 and compo1_cnt > 0 and compo2_cnt > 0:
                        return True
    return False


victories = 0
for i in range(1, 9):
    for j in range(i + 1, 10):
        if check(i, j):
            victories += 1

print(victories)