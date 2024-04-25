n, m = map(int, input().split())
arr = list(map(int, input().split()))


for _ in range(m):
    ans = 0
    a, b = map(int, input().split())
    for i in range(a - 1, b):
        ans += arr[i]

    print(ans)