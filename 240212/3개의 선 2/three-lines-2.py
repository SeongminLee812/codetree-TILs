n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

combi = [('x', 'x', 'x'), ('x', 'x', 'y'), ('x', 'y', 'y'), ('y', 'y', 'y')]

def check(direction, position, point):
    if direction == 'x':
        if point[0] == position:
            return True
    else:
        if point[1] == position:
            return True
    return False

ok = 0
for line1, line2, line3 in combi:
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for point in points:
                    if check(line1, i, point) and check(line2, j, point) and check(line3, k, point):
                        ok = 1

print(ok)