from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

already = defaultdict(int)

result = []
for i in range(n):
    i_rank = 1
    for j in range(n):
        if i == j:
            continue
        if arr[i] > arr[j]:
            i_rank += 1
    result.append(i_rank + already[arr[i]])
    already[arr[i]] += 1

print(' '.join(map(str, result)))