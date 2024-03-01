n = int(input())

segments = []
a_list = []
b_list = []

for _ in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    segments.append((a, b))

max_a = max(a_list)
min_b = min(b_list)

if max_a <= min_b:
    print('Yes')
else:
    print('No')