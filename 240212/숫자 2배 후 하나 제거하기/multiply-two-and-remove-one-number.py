import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        remaining_arr = [elem for idx, elem in enumerate(arr) if idx != j]
        value = 0
        for k in range(1, len(remaining_arr)):
            diff = abs(remaining_arr[k - 1] - remaining_arr[k])
            value += diff
        ans = min(ans, value)

    arr[i] //= 2

print(ans)