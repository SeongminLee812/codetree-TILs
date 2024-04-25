n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
length = 0
for i in range(n):
    if arr[i] > t:
        length += 1
    else:
        ans = max(ans, length)
        length = 0
    print(length, end=' ')

print(ans)