n = int(input())
a = list(map(int, input().split()))

max_val = 0

for i in range(n - 2):
    for j in range(i + 2, n):
        sum_val = a[i] + a[j]
        max_val = max(max_val, sum_val)

print(max_val)