n, l = map(int, input().split())
arr = list(map(int, input().split()))
MAX_INT = 100

def is_possible(limit_h):
    cnt = 0
    minus_1_cnt = 0
    for i in range(n):
        if arr[i] >= limit_h:
            cnt += 1
        if arr[i]== limit_h - 1:
            minus_1_cnt += 1

    if minus_1_cnt >= l:
        limit_h -= l
    elif minus_1_cnt < l:
        limit_h -= minus_1_cnt

    if cnt >= limit_h:
        return True

    return False

ans = 0
for i in range(MAX_INT + 1):
    if is_possible(i):
        ans = i

print(ans)