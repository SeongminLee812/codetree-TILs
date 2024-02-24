n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr = [0] * 101

for x1, x2 in segments:
    for i in range(x1, x2 + 1):
        arr[i] += 1

print(max(arr))