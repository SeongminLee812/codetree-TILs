import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

# 합으로 가능한 최소값을 limit으로 지정
for limit in range(max(arr), 100 * 100 + 1):
    now_val = 0
    partition = 0
    max_val = 0
    # arr의 앞에서부터 탐색
    for i in range(n):
        if now_val + arr[i] > limit:
            now_val = 0
            partition += 1

        now_val += arr[i]
        max_val = max(now_val, max_val)

    if partition <= m - 1:
        ans = min(ans, max_val)

print(ans)