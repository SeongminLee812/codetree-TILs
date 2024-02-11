n = int(input())

arr = list(map(int, input().split()))
arr.sort()


ans = 0
for k in range(min(arr) + 1, max(arr)):
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if k - arr[i] == arr[j] - k:
                cnt += 1
    ans = max(ans, cnt)

print(ans)