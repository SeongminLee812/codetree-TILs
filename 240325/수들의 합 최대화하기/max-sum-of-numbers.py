n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

picked = []

visited_row = [False] * n
visited_col = [False] * n

def calc():
    value = 0
    for i, j in picked:
        value += arr[i][j]
    return value

def choose(cnt):
    # picked의 cnt번째 수를 결정하는 함수
    global ans

    if cnt == n + 1:
        ans = max(ans, calc())
        return

    for i in range(n):
        if visited_row[i]:
            continue
        visited_row[i] = True

        for j in range(n):
            if visited_col[j]:
                continue

            visited_col[j] = True
            picked.append((i, j))

            choose(cnt + 1)
            visited_col[j] = False
            picked.pop()

        visited_row[i] = False

ans = 0
choose(1)
print(ans)