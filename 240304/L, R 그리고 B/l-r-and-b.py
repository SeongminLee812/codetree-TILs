import sys

arr = [
    list(input())
    for _ in range(10)
]

L = [0, 0]
B = [0, 0]
R = [0, 0]

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'L':
            L[0], L[1] = i, j
        elif arr[i][j] == 'B':
            B[0], B[1] = i, j
        elif arr[i][j] == 'R':
            R[0], R[1] = i, j

dist = abs(L[0] - B[0]) + abs(L[1] - B[1]) - 1

if dist == 0:
    print(dist)
    sys.exit()


if L[0] == B[0] == R[0] and (L[1] < R[1] < B[1] or B[1] < R[1] < L[1]):
    dist += 2
elif L[1] == B[1] == R[1] and (L[0] < R[0] < B[0] or B[0] < R[0] < L[0]):
    dist += 2

print(dist)