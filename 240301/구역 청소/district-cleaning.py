a, b = map(int, input().split())
c, d = map(int, input().split())

MAX_INT = 100

arr = [0] * (MAX_INT + 1)
for i in range(a, b):
    arr[i] = 1
for i in range(c, d):
    arr[i] = 1

print(sum(arr))