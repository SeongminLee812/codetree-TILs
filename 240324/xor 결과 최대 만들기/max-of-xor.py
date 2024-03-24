import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
def choose(num_index, cnt, xor):
    global ans

    if cnt == m:
        ans = max(xor, ans)
        return
    if num_index == n:
        return

    # 선택
    choose(num_index + 1, cnt + 1, xor ^ arr[num_index])
    # 미선택
    choose(num_index + 1, cnt, xor)

choose(0, 0, 0)

print(ans)