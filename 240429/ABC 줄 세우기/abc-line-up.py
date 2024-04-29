n = int(input())
arr = list(input().split())
arr = list(map(ord, arr))

def insertion_sort():
    global ans
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            ans += 1
            j -= 1
        arr[j + 1] = temp

ans = 0
insertion_sort()
print(ans)