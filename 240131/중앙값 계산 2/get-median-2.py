n = int(input())

arr = list(map(int, input().split()))

for i in range(1, n + 1, 2):
    temp_arr = arr[:i]
    temp_arr.sort()
    print(temp_arr[i//2], end=' ')