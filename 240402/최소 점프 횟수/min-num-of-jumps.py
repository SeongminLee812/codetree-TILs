import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize

def choose(curr_index_in_arr, cnt):
    global ans
    if curr_index_in_arr >= n - 1:
        ans = min(ans, cnt)
        return

    for i in range(1, arr[curr_index_in_arr] + 1):
        choose(curr_index_in_arr + i, cnt + 1)

choose(0, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)