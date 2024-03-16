n = int(input())
x, y = map(int, input().split())
arr = [
    list(input())
    for _ in range(n)
]

def out_of_grid(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def is_wall(x, y):
    wall_dir = (dir_num + 1) % 4
    wall_x = x + dx[wall_dir]
    wall_y = y + dy[wall_dir]
    if arr[wall_x][wall_y] == '#':
        return True
    return False

t = 0
x -= 1
y -= 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num = 0

visited = [
    [False] * n
    for _ in range(n)
]
visited[x][y] = True

left_turn = 0
right_turn = 0

while True:
    if is_wall(x, y):
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if out_of_grid(nx, ny):
            t += 1
            break
        elif arr[nx][ny] == '#':
            dir_num = (dir_num - 1 + 4) % 4
            left_turn += 1
            right_turn = 0
        elif arr[nx][ny] == '.':
            # 이동하려한 공간이 이미 방문한 곳일 때(탈출 불가)
            # if visited[nx][ny]:
            #     t = -1
            #     break
            # 방문한 적이 없다면
            visited[nx][ny] = True
            x = nx
            y = ny
            t += 1

    else:
        dir_num = (dir_num + 1) % 4
        left_turn = 0
        right_turn += 1
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        x = nx
        y = ny
        t += 1

    if t > 10000 or left_turn > 4 or right_turn > 4:
        t = -1
        break
        

print(t)