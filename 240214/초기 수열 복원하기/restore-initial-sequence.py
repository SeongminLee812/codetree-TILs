n = int(input())
sum_arr = list(map(int, input().split()))

result = [0] * n

for i in range(1, n):
    exist = [False] * (n + 1)
    result[0] = i
    ok = True
    for j in range(1, n):
        result[j] = sum_arr[j - 1] - result[j - 1]

        if result[j] <= 0 or result[j] > n:
            ok = False
            break
        else:
            if exist[result[j]]:
                ok = False
                break
        exist[result[j]] = True

    if ok:
        print(' '.join(map(str, result)))
        break