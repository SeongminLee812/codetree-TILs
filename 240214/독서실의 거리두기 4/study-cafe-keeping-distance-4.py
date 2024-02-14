import sys

n = int(input())
arr = list(map(int, input()))

def minimun_distance():
    """가장 가까운 두 사람"""
    dist = n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == 1 and arr[j] == 1:
                dist = min(dist, j - i)


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