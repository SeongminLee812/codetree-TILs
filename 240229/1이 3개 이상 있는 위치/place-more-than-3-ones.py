n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

max_cnt = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        x, y = i, j
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        
        max_cnt = max(cnt, max_cnt)

print(max_cnt)