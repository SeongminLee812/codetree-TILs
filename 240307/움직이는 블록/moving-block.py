import sys

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

def find_second(max_val):
    second_val = 0
    for i in range(n):
        if arr[i] < max_val and arr[i] > second_val:
            second_val = arr[i]
    try:
        return second_val
    except:
        return False

def find_max():
    max_val = 0
    min_val = sys.maxsize
    max_idx = 0
    min_idx = 0

    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    if max_val == min_val:
        return False
    return max_val, max_idx, min_val, min_idx

cnt = 0
while True:
    value_tuple = find_max()
    if not value_tuple:
        break
    else:
        max_val, max_idx, min_val, min_idx = value_tuple

    second_val = find_second(max_val)
    diff = max_val - second_val
    arr[min_idx] += diff
    arr[max_idx] -= diff
    cnt += diff
    print(arr)

print(cnt)