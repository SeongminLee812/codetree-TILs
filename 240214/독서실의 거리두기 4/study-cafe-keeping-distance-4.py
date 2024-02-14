import sys

n = int(input())
arr = list(map(int, input()))

def minimun_distance():
    """가장 가까운 두 사람"""
    min_dist = sys.maxsize
    for i in range(n):
        if arr[i] == 1:
            prev_i = i
            break
    for i in range(prev_i + 1, n):
        if arr[i] == 1:
            dist = i - prev_i
            min_dist = min(min_dist, dist)
            prev_i = i
    return min_dist


max_dist = 0
for i in range(n - 1):
    if arr[i] == 0:
        arr[i] = 1
        for j in range(i + 1, n):
            if arr[j] == 0:
                arr[j] = 1
                dist = minimun_distance()
                max_dist = max(max_dist, dist)
                arr[j] = 0

        arr[i] = 0

print(max_dist)