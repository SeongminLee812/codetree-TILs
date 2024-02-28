dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y = 0, 0
dir_num = 0
dir_dict = {'W': 0, 'S': 1, 'N': 2, 'E': 3}


n = int(input())
for _ in range(n):
    direction, move = input().split()
    move = int(move)
    dir_num = dir_dict[direction]

    for _ in range(move):
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        x, y = nx, ny

print(x, y)