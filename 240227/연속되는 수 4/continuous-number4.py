n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

ans = 1
cnt = 1

for i in range(n):
    if i == 0:
        continue
    if arr[i - 1] < arr[i]:
        cnt += 1
    if arr[i - 1] >= arr[i] or i == n - 1:
        ans = max(ans, cnt)
        cnt = 1

print(ans)