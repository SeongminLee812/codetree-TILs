n, m = map(int, input().split())
arr = list(map(int, input().split()))

window_size = m * 2 + 1

wifi = 0
i = 0

while i < n:
    if arr[i] == 1:
        wifi += 1
        i += window_size
    else:
        i += 1

print(wifi)