import copy
from collections import defaultdict

n, m = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

beautiful = defaultdict(int)
for i in range(m):
    beautiful[arr_b[i]] += 1

def check(num_array, check_dict):
    check_dict = copy.deepcopy(check_dict)
    for i in range(len(num_array)):
        check_dict[num_array[i]] -= 1
        if check_dict[num_array[i]] < 0:
            return False

    for value in check_dict.values():
        if value != 0:
            return False
    return True


ans = 0
for i in range(n):
    for j in range(i, n):
        elems = arr_a[i:j + 1]
        if check(elems, beautiful):
            ans += 1

print(ans)