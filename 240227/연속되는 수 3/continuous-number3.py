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
    # 부호가 같은 경우
    if arr[i - 1] * arr[i] > 0:
        cnt += 1
    # different sign or final num
    # calculrate ans
    if arr[i - 1] * arr[i] < 0 or i == n - 1:
        ans = max(ans, cnt)
        cnt = 1

print(ans)