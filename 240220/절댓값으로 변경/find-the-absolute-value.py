n = int(input())
arr = list(map(int, input().split()))

def abs_list(array):
    for i in range(n):
        array[i] = abs(array[i])

abs_list(arr)
print(' '.join(map(str, arr)))