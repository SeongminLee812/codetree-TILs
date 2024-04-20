import sys

n = int(input())
arr = list(map(int, input().split()))

def go(visit):
    global ans
    if visit >= n - 1:
        ans = min(ans, len(selected))
        return

    for i in range(1, arr[visit] + 1):
        selected.append(visit)
        go(visit + i)
        selected.pop()


ans = sys.maxsize
selected = []

go(0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)