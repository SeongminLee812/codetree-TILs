n = int(input())

arr = [0] * (200 + 1)

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for x1, x2 in segments:
    x1, x2 = x1 + 100, x2 + 100

    for i in range(x1, x2):
        arr[i] += 1

print(max(arr))