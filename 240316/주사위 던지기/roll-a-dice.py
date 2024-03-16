n, m, r, c = map(int, input().split())
directions = list(input().split())
arr = [
    [0] * n
    for _ in range(n)
]

dice = {
    'now': 6,
    'U': 5,
    'D': 2,
    'L': 4,
    'R': 3
}

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def rotate(direction):
    if direction == 'L':
        new = dice['L']
        dice['R'] = dice['now']
        dice['L'] = 7 - dice['R']
        dice['now'] = new
    elif direction == 'R':
        new = dice['R']
        dice['L'] = dice['now']
        dice['R'] = 7 - dice['L']
        dice['now'] = new
    elif direction == 'U':
        new = dice['U']
        dice['D'] = dice['now']
        dice['U'] = 7 - dice['D']
        dice['now'] = new
    elif direction == 'D':
        new = dice['D']
        dice['U'] = dice['now']
        dice['D'] = 7 - dice['U']
        dice['now'] = new

dir_num = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

x = r - 1
y = c - 1
arr[x][y] = dice['now']
for d in directions:
    dir_num = dir_dict[d]
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if in_range(nx, ny):
        rotate(d)
        arr[nx][ny] = dice['now']
        x, y = nx, ny

ans = 0
for line in arr:
    ans += sum(line)

print(ans)