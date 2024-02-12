import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


def count(x_line, y_line):
    area_1, area_2, area_3, area_4 = 0, 0, 0, 0
    for x, y in points:
        if x > x_line and y > y_line:
            area_1 += 1
        elif x > x_line and y < y_line:
            area_4 += 1
        elif x < x_line and y > y_line:
            area_2 += 1
        else:
            area_3 += 1
    return area_1, area_2, area_3, area_4

ans = sys.maxsize

for x_line in range(2, 101, 2):
    for y_line in range(2, 101, 2):
        counts = count(x_line, y_line)
        max_area = max(counts)
        ans = min(ans, max_area)

print(ans)