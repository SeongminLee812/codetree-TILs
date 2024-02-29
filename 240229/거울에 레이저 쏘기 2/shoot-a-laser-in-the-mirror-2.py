n = int(input())
arr = [
    list(input())
    for _ in range(n)
]

start = int(input())

# define function which return if x, y in range
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# define move function
def move(dir_num):
    global cnt
    global x, y
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    cnt += 1
    x, y = nx, ny

# transform start point to coordinate
if (start) // n <= 0:
    dir_num = 2
    x = 0
    y = (start - 1) % n
elif (start) // n <= 1:
    dir_num = 1
    x = (start - 1) % n
    y = n - 1
elif (start) // n <= 2:
    dir_num = 0
    x = n - 1
    y = n - 1 - ((start - 1) % n)
else:
    dir_num = 3
    x = n - 1 - ((start - 1) % n)
    y = 0


cnt = 0
while in_range(x, y):

    if arr[x][y] == '/':
        if dir_num == 0:
            dir_num = 3
        elif dir_num == 1:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 1
        elif dir_num == 3:
            dir_num = 0
        move(dir_num)
    else:
        if dir_num == 0:
            dir_num = 1
        elif dir_num == 1:
            dir_num = 0
        elif dir_num == 2:
            dir_num = 3
        elif dir_num == 3:
            dir_num = 2
        move(dir_num)

print(cnt)