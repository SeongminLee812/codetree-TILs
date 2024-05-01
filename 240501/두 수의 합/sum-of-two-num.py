from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count_dict = Counter(arr)

ans = 0

for x in arr:
    if x == k - x:
        ans += count_dict[k - x] - 1
    else:
        ans += count_dict[k - x]
    if count_dict[x] > 0:
        count_dict[x] -= 1

print(ans)