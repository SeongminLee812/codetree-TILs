n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
print(' '.join(map(str, arr)))
print(' '.join(map(str, arr[::-1])))