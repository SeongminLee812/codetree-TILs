n, m = map(int, input().split())

a = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

# define function if in range
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

x, y = 0, 0
a[x][y] = 'A'

# to transform num to alpha
diff = ord('Z') - ord('A') + 1
num_a = ord('A')

for i in range(1, n * m):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny) or a[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x += dx[dir_num]
    y += dy[dir_num]
    alpha = i % diff + num_a
    a[x][y] = chr(alpha)

for line in a:
    print(" ".join(map(str, line)))