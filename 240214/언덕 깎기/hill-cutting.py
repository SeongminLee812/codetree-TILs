import sys

n = int(input())
mount = [int(input()) for _ in range(n)]

def check_cost(min_height):
    cost = 0
    for elem in mount:
        if elem > min_height + 17:
            cost += (elem - (min_height + 17)) ** 2
        elif elem < min_height:
            cost += (min_height - elem) ** 2
    return cost

min_cost = sys.maxsize
for i in range(0, max(mount) +1):
    min_cost = min(min_cost, check_cost(i))

print(min_cost)