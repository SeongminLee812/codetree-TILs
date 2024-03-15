n = int(input())
arr = [
    int(input())
    for _ in range(n)
]


for _ in range(2):
    s1, e1 = map(int, input().split())
    s1 -= 1
    e1 -= 1

    temp_array = [0] * n

    temp_idx = 0
    for i in range(n):
        if s1 <= i <= e1:
            continue

        temp_array[temp_idx] = arr[i]
        temp_idx += 1
    arr = temp_array

print(len([i for i in arr if i]))
for elem in arr:
    if elem:
        print(elem)