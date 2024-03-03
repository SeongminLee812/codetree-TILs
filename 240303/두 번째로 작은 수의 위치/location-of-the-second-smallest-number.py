import sys

n = int(input())
arr = list(map(int, input().split()))

min_val = min(arr)
second_val = 0
second_idx = -1

if min_val == max(arr):
    print(-1)
    sys.exit()

for i in range(n):
    if not second_val and arr[i] > min_val:
        second_val = arr[i]
        second_idx = i

    elif arr[i] > min_val and arr[i] < second_val:
        second_val = arr[i]
        second_idx = i

    elif arr[i] == second_val:
        second_idx = -1

if second_idx >= 0:
    second_idx += 1
print(second_idx)