import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize

def choose(curr_pos, cnt):
    global ans
    if curr_pos >= n - 1:
        ans = min(ans, cnt)
        return

    for i in range(1, arr[curr_pos] + 1):
        choose(curr_pos + i, cnt + 1)

choose(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)