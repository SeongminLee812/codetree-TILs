n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

arr.sort(key=lambda x:x[0])

for i in range(n):
    if arr[i][2] == 'Rain':
        print(' '.join(arr[i]))
        break