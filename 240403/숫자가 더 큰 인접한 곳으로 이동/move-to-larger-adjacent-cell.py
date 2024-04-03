n, r, c = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = []

r, c = r - 1, c - 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

visited.append((r, c))
prev_pos = r, c
curr_pos = r, c

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

while True:
    x, y = curr_pos
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            curr_pos = nx, ny
            visited.append((nx, ny))
            break
    if prev_pos == curr_pos:
        break
    prev_pos = curr_pos

for x, y in visited:
    print(arr[x][y], end=' ')