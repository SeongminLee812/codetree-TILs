import sys

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = sys.maxsize

for i in range(n):
    size = 0
    xs = []
    ys = []
    for j in range(n):
        if i == j:
            continue
        x, y = points[j]
        xs.append(x)
        ys.append(y)
    size = (max(xs) - min(xs)) * (max(ys) - min(ys))
    ans = min(ans, size)

print(ans)