dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

directions = ['W', 'S', 'N', 'E']

n = int(input())

x, y = 0, 0
for _ in range(n):
    direction, times = input().split()
    times = int(times)
    for i in range(4):
        if direction == directions[i]:
            nx = dx[i] * times
            ny = dy[i] * times
    x += nx
    y += ny

print(x, y)