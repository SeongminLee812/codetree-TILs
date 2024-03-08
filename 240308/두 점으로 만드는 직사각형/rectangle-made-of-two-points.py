x1, y1, x2, y2 = map(int, input().split())
a1, b1, c1, d1 = map(int, input().split())

width = max([x1, x2, a1, c1]) - min([x1, x2, a1, c1])
height = max([y1, y2, b1, d1]) - min([y1, y2, b1, d1])

print(width * height)