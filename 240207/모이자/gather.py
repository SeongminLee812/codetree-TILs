import sys

n = int(input())
a = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += abs(a[i] - a[j]) * j
    min_val = min(min_val, sum_val)

print(min_val)