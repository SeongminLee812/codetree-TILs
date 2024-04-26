# 북쪽에서 시작
# dxs, dys 잘 정의해서 왼쪽 -> 시계반대방향, 오른쪽 -> 시계방향으로 회전할 수 있도록 위치시키기
n, t = map(int, input().split())
directions = list(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

dir_num = 0

x, y = n // 2, n // 2
ans = arr[x][y]

for i in range(t):
    if directions[i] == 'L':
        dir_num = (dir_num + 4 - 1) % 4
    elif directions[i] == 'R':
        dir_num = (dir_num + 1) % 4
    elif directions[i] == 'F':
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if in_range(nx, ny):
            ans += arr[nx][ny]
            x, y = nx, ny

print(ans)