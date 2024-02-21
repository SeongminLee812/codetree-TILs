n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0
for i in range(n):
    first, second = i, 2 * n - i - 1
    val = arr[first] + arr[second]
    ans = max(ans, val)

print(ans)