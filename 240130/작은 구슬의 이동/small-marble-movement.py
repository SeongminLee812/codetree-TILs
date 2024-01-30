n, t = map(int, input().split())
r, c, d = input().split()
r, c = map(int, [r, c])

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

dire = {'L': 0, 'R': 3, 'U': 2, 'D': 1}

move_num = dire[d]

def in_range(x, y):
    return x >= 1 and x < n and y >= 1 and y < n

x, y = r, c

while t:
    nx = x + dx[move_num]
    ny = y + dy[move_num]
    if not in_range(nx, ny):
        move_num = 3 - move_num
    else:
        x = nx
        y = ny
    t -= 1

print(x, y)