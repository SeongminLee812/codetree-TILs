n = int(input())

min_idx = 0
min_val = 101
second_min_val = 101

max_idx = 0
max_val = 0
second_max_val = 0

for i in range(n):
    x1, x2 = map(int, input().split())
    if x1 < min_val:
        min_val = x1
        min_idx = i
    elif x1 < second_min_val:
        second_min_val = x1
    if x2 > max_val:
        max_val = x2
        max_idx = i
    elif x2 > second_max_val:
        second_max_val = x2

candidates = [second_max_val - min_val,
              max_val - second_min_val]

print(min(candidates))