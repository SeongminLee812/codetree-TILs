# idea
# if check(nx) or not in_range(nx):
# direction += 1

# case 1: 그 다음위치가 격자를 벗어나지는 않는지
# case 2: 이미 방문했던 곳은 아닌지

# 방향을 90도 돌리기 -> (dir + 1) % 4

n, m = map(int, input().split())

a = [[0] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num = 0

x, y = 0, 0

now = 0
while True:
    now += 1
    a[x][y] = now 
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny) or a[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

    if not in_range(nx, ny) or a[nx][ny] != 0:
        break
    
    x = nx
    y = ny

for line in a:
    print(' '.join(map(str, line)))


        

# 순서가 어떻게?
## 현재 자기 자신 += 1 -> 방향대로 이동 가능한지 확인 -> 이동불가능하면 방향 전환
## 방향 전환 후 다시 이동 가능한 지 확인: 이동 불가능하면 종료, 이동가능하면 이동