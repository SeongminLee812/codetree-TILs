n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 합으로 가능한 최소값을 limit으로 지정
for limit in range(1, 100 * 100 + 1):
    # arr의 앞에서부터 탐색
    prev_i = 0
    partition = 0
    for i in range(n):
        if limit < sum(arr[prev_i: i + 1]):
            partition += 1
            prev_i = i

    if partition == m - 1:
        limit = max(limit, max(arr))
        print(limit)
        break