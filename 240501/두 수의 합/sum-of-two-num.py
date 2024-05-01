from collections import Counter, defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count_dict = defaultdict(int)

ans = 0

for elem in arr:
    diff = k - elem
    if diff in count_dict:
        ans += count_dict[diff]

    count_dict[elem] += 1

print(ans)