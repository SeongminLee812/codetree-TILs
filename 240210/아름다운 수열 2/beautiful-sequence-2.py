import copy
from collections import defaultdict

n, m = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

check_array = sorted(arr_b)


ans = 0
for i in range(n - m + 1):
    if sorted(arr_a[i: i + m]) == check_array:
        ans += 1

print(ans)