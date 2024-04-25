from collections import defaultdict

n = int(input())
arr = ['G'] * 200000
now = 100000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'R':
        for i in range(now, now + x):
            arr[i] = 'B'
        now = i

    else:
        for i in range(now, now - x, -1):
            arr[i] = 'W'
        now = i

ans_dict = defaultdict(int)
for i in range(200000):
    if arr[i] == 'W':
        ans_dict['W'] += 1
    elif arr[i] == 'B':
        ans_dict['B'] += 1

print(ans_dict['W'], ans_dict['B'])