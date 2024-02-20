def all_sum(arr, m):
    result = 0
    while m > 1:
        result += arr[m - 1]
        if m % 2 == 0:
            m //=2
        else:
            m -= 1
    result += arr[m - 1]
    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(all_sum(arr, m))