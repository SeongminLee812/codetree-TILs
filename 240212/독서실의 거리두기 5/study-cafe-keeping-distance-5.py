import sys

n = int(input())

arr = list(map(int, input()))

def cal_dist(array):
    min_diff = sys.maxsize
    prev_i = 0
    first_1 = True
    for i in range(0, len(array)):
        if array[i] == 1:
            if first_1:
                prev_i = i
                first_1 = False
                continue
            diff = i - prev_i
            prev_i = i
            min_diff = min(diff, min_diff)
    return min_diff

ans = 0

for i in range(n):
    # 새로운 한명 투입 가능 여부 확인
    dist = 0
    if i == n - 1:
        if arr[i] == 0 and arr[i - 1] == 0:
            arr[i] = 1
            dist = cal_dist(arr)
            arr[i] = 0
    if i == 0:
        if arr[i] == 0 and arr[i + 1] == 0:
            arr[i] = 1
            dist = cal_dist(arr)
            arr[i] = 0
    elif arr[i] == 0 and arr[i - 1] == 0 and arr[i + 1] == 0:
        arr[i] = 1
        dist = cal_dist(arr)
        arr[i] = 0

    ans = max(ans, dist)

print(ans)