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
    elif direction == 'y':
        if point[1] == position:
            return True
    return False

ok = 0
for line1, line2, line3 in combi:
    for i in range(11):
        for j in range(11):
            for k in range(11):
                cnt = 0
                for point in points:
                    # 모든 포인트를 다 검사 해야함
                    if check(line1, i, point) or check(line2, j, point) or check(line3, k, point):
                        cnt += 1
                if cnt == n:
                    ok = 1


print(ok)