x, y = 0, 0

n = int(input())
t = 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dir_num = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

def go():
    global x, y, t
    for _ in range(n):
        direct, num = input().split()
        num = int(num)
        for _ in range(num):
            x += dxs[dir_num[direct]]
            y += dys[dir_num[direct]]
            t += 1
            if x == 0 and y == 0:
                print(t)
                not_found = False
                return
    print(-1)
go()