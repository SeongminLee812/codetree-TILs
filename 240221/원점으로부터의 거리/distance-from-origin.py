from functools import cmp_to_key

def compare(first, second):
    if abs(first.x) + abs(first.y) < abs(second.x) + abs(second.y):
        return -1
    if abs(first.x) + abs(first.y) > abs(second.x) + abs(second.y):
        return 1
    return 0

class Coordinate():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

    def __repr__(self):
        return  f'{self.num}'

n = int(input())
coors = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    coors.append(Coordinate(x, y, i))

coors.sort(key=cmp_to_key(compare))
for c in coors:
    print(c)