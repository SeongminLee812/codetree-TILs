import sys

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

INT_MAX = sys.maxsize
ans = INT_MAX

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

for i in range(n - 1):
    for j in range(i + 1, n):
        dist = distance(points[i], points[j])
        ans = min(dist, ans)

print(ans)