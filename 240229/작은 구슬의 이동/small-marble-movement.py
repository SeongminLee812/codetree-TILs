n, t = map(int, input().split())

x, y, d = input().split()
x, y = int(x) - 1, int(y) - 1

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

dir_dict = {
    'U': 0,
    'D': 3,
    'R': 2,
    'L': 1
}

dir_num = dir_dict[d]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

while t:
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if in_range(nx, ny):
        x, y = nx, ny
        t -= 1
    else:
        dir_num = 3 - dir_num
        t -= 1

print(x + 1, y + 1)