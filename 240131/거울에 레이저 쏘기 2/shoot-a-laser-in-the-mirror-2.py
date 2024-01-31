# 방향 정의
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 거울을 만났을 때 변하는 방향 정의
front_dir = {0: 3, 1: 2, 2: 1, 3: 0}
back_dir = {0: 1, 1: 0, 2: 3, 3: 2}

# in_range 함수 정의
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 입력받기
n = int(input())
a = [list(input()) for _ in range(n)]
k = int(input())

def set_k(k):
    if k <= n:
        dir_num = 1
        coor = (0, (k - 1) % n)
    elif k <= n * 2:
        dir_num = 0
        coor = ((k - 1) % n, n - 1)
    elif k <= n * 3:
        dir_num = 3
        coor = (n - 1, n - 1 - (k - 1) % n)
    else:
        dir_num = 2
        coor = (n - 1 - (k - 1) % n, 0)
    return dir_num, coor

t = 0

# m 입력 받아서 x, y 그리고 dir_num 정의

dir_num, (x, y) = set_k(k)

while in_range(x, y):
    # print(f'x = {x}, y = {y}, dir_num = {dir_num}')
    mirror = a[x][y]

    if mirror == '/':
        dir_num = front_dir[dir_num]
    else:
        dir_num = back_dir[dir_num]
    x += dx[dir_num]
    y += dy[dir_num]
    dir_num = (dir_num + 2) % 4
    t += 1
    if t == 10:
        break
print(t)