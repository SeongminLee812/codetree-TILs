import sys

n = int(input())
a = [0] + list(map(int, input().split()))

min_val = sys.maxsize

for i in range(1, n + 1):
    sum_val = 0
    for j in range(1, n + 1):
        sum_val += abs(i - j) * a[j]
    min_val = min(min_val, sum_val)

print(min_val)