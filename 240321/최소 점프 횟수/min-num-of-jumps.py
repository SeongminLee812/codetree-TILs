import sys

# 현재 array의 위치를 받아서 curr_index를 순회
n = int(input())
arr = list(map(int, input().split()))

def go(curr_index, cnt):
    global ans
    if curr_index >= n - 1:
        ans = min(cnt, ans)
        return

    for i in range(1, arr[curr_index] + 1):
        go(curr_index + i, cnt + 1)

ans = sys.maxsize

go(0, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)