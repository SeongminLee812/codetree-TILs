n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bomb(x, y):
    bomb_range = arr[x][y]
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    arr[x][y] = 0

    for br in range(1, bomb_range):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + (dx * br), y + (dy * br)
            if in_range(nx, ny):
                arr[nx][ny] = 0

def gravitify():
    for col in range(n):
        temp = [0] * n
        temp_index = n - 1
        for row in range(n - 1, -1, -1):
            if arr[row][col]:
                temp[temp_index] = arr[row][col]
                temp_index -= 1
        for i in range(n):
            arr[i][col] = temp[i]


bomb(r - 1, c - 1)
gravitify()
for line in arr:
    print(' '.join(map(str, line)))