from collections import defaultdict

n = int(input())
arr = ['G'] * 200000
now = 100000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'R':
        while x:
            arr[now] = 'B'
            now += 1
            x -= 1

    else:
        while x:
            arr[now] = 'W'
            now -= 1
            x -= 1



ans_dict = defaultdict(int)
for i in range(200000):
    if arr[i] == 'W':
        ans_dict['W'] += 1
    elif arr[i] == 'B':
        ans_dict['B'] += 1

print(ans_dict['W'], ans_dict['B'])