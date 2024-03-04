import sys

n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)
if max_val == min_val:
    print(-1)
    sys.exit()

second_val = sys.maxsize

for i in range(n):
    if arr[i] > min_val and arr[i] < second_val:
        second_idx = i
        second_val = arr[i]
        cnt = 1
    elif arr[i] == second_val:
        cnt += 1

if cnt >= 2:
    print(-1)
else:
    print(second_idx + 1)