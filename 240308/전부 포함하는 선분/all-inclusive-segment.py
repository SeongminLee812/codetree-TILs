n = int(input())

x1_list = []
x2_list = []

for i in range(n):
    x1, x2 = map(int, input().split())
    x1_list.append(x1)
    x2_list.append(x2)

x1_list.sort()
x2_list.sort(key=lambda x: -x)
min_val, second_min_val = x1_list[0], x1_list[1]
max_val, second_max_val = x2_list[0], x2_list[1]

candidates = [second_max_val - min_val,
              max_val - second_min_val]

print(min(candidates))