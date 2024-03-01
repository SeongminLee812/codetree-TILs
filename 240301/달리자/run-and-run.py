n = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

total = 0
for i in range(n - 1):
    if arr_a[i] > arr_b[i]:
        diff = arr_a[i] - arr_b[i]
        arr_a[i] -= diff
        arr_a[i + 1] += diff
        # 이동량
        total += diff

print(total)