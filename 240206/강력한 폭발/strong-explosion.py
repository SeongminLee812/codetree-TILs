n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

bomb_position = []
bomb_num = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            bomb_position.append((i, j))
            bomb_num += 1

# bomb shape 에 따른 dx, dy 정의
def dx_dy(bomb_shape: int):
    if bomb_shape == 1:
        dx = [0, -1, -2, 1, 2]
        dy = [0, 0, 0, 0, 0]
    elif bomb_shape == 2:
        dx = [0, -1, 1, 0, 0]
        dy = [0, 0, 0, -1, 1]
    else:
        dx = [0, -1, -1, 1, 1]
        dy = [0, -1, 1, -1, 1]
    return dx, dy

#dx dy 이동이 가능한지 판단하는 함수
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

# 경우의수 골라내기
bombs_shape = []
chosen = []

def choose(index):
    global bombs_shape, chosen
    if index == bomb_num:
        bombs_shape.append(tuple(chosen))
        return
    for i in range(1, 3 + 1):
        chosen.append(i)
        choose(index + 1)
        chosen.pop()


choose(0)

answer = 0

for bombs in bombs_shape:
    visited = [[False] * n for _ in range(n)]
    total = 0
    for shape, pos in zip(bombs, bomb_position):
        dx, dy = dx_dy(shape)
        bomb_x, bomb_y = pos
        for i in range(len(dx)):
            nx = bomb_x + dx[i]
            ny = bomb_y + dy[i]
            if can_go(nx, ny):
                visited[nx][ny] = True
                total += 1

    answer = max(answer, total)

print(answer)