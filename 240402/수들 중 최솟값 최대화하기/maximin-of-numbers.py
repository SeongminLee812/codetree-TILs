import sys

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False] * n

def calc():
    value = sys.maxsize
    for i in range(n):
        value = min(value, arr[i][col[i]])
    return value

def choose(row_index):
    global ans
    if row_index == n:
        ans = max(ans, calc())
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        col.append(i)
        choose(row_index + 1)
        col.pop()
        visited[i] = False

ans = 0
col = []
choose(0)
print(ans)