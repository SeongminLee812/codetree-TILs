n = int(input())
input_arr = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append(input_arr[i])

    if i == 0:
        print(arr[i], end=' ')
        continue

    key = arr[-1]
    j = len(arr) - 2
    while arr[j] > key and j >= 0:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

    if i % 2 == 0:
        print(arr[i // 2], end=' ')