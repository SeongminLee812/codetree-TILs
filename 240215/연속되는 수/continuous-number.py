n = int(input())
arr = [int(input()) for _ in range(n)]

candidate = sorted(list(set(arr)))

ans = 0
for i in range(len(candidate)):
    cnt = 1
    prev_index = 0
    for j in range(n):
        if arr[j] == candidate[i]:
            continue

        if arr[j] == arr[prev_index]:
            cnt += 1
        else:
            cnt = 1
        prev_index = j
        ans = max(ans, cnt)

print(ans)