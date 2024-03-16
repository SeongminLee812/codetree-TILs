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

visited =[
    [
        [False] * 4
        for _ in range(n)
    ]
    for _ in range(n)
]

while True:
    if visited[x][y][dir_num]:
        t = -1
        break
    visited[x][y][dir_num] = True

    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if out_of_grid(nx, ny):
        t += 1
        break
    elif arr[nx][ny] == '#':
        dir_num = (dir_num - 1 + 4) % 4
    elif arr[nx][ny] == '.':
        if is_wall(nx, ny):
            x = nx
            y = ny
            t += 1
        else:
            dir_num = (dir_num + 1) % 4
            nx = nx + dx[dir_num]
            ny = ny + dy[dir_num]
            x = nx
            y = ny
            t += 2
print(t)