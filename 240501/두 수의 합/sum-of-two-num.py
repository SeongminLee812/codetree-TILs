from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count_dict = defaultdict(int)

for i in range(n):
    count_dict[k - arr[i]] += 1

ans = 0
for i in range(n):
    ans += count_dict[arr[i]]
print(ans // 2)