n = int(input())
a = list(map(int, input().split()))

def max_val(n):
    if n == 0:
        return a[n]
    before_val = max_val(n - 1)
    if before_val < a[n]:
        return a[n]
    else:
        return before_val

print(max_val(n - 1))