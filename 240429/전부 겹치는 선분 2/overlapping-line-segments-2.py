import sys

n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]



for skip in range(n):
    max_x1, min_x2 = 0, sys.maxsize
    okay = False
    for i in range(n):
        if skip == i:
            continue



        max_x1 = max(max_x1, arr[i][0])
        min_x2 = min(min_x2, arr[i][1])

    if min_x2 >= max_x1:
        okay = True
        break

if okay:
    print('Yes')
else:
    print('No')