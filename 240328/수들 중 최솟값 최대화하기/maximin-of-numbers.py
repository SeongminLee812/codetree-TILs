# 각 행에서 열을 순서대로 선택만 하면됨.
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

INT_MAX = 10001
visited = [False for _ in range(n)]
picked = []

ans = 0

def choose(row):
    global ans
    if row == n:
        min_val = INT_MAX
        for i in range(n):
            if arr[i][picked[i]] < min_val:
                min_val = arr[i][picked[i]]
        ans = max(ans, min_val)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        picked.append(i)

        choose(row + 1)

        visited[i] = False
        picked.pop()
        
choose(0)
print(ans)