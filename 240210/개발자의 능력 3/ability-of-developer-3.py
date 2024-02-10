import sys

arr = list(map(int, input().split()))

all_sum = sum(arr)
ans = sys.maxsize
for i in range(0, 6 - 2):
    for j in range(i + 1, 6 - 1):
        for k in range(j + 1, 6):
            sum1 = arr[i] + arr[j] + arr[k]
            sum2 = all_sum - sum1
            diff = abs(sum1 - sum2)
            ans = min(ans, diff)

print(ans)