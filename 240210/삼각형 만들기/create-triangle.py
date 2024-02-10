import sys
INT_MAX = sys.maxsize

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

def cal_size(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # condition
    if (y1 == y2 or y2 == y3 or y1 == y3) and (x1 == x2 or x2 == x3 or x1 == x3):
        size = abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))
        return size
    return 0

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            size = cal_size(points[i], points[j], points[k])
            ans = max(size, ans)


print(ans)