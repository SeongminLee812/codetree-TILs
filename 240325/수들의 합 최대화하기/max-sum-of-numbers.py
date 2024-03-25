n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

picked_row = []
picked_col = []

visited_row = [False] * n
visited_col = [False] * n

def calc():
    value = 0
    for i, j in zip(picked_row, picked_col):
        value += arr[i][j]
    return value

def choose(row_cnt, col_cnt):
    # picked의 cnt번째 수를 결정하는 함수
    global ans
    combi = 0

    if row_cnt == col_cnt == n + 1:
        ans = max(ans, calc())
        combi += 1
        return

    if row_cnt <= n:
        for i in range(n):
            if visited_row[i]:
                continue
            visited_row[i] = True
            picked_row.append(i)
            choose(row_cnt + 1, col_cnt)

            picked_row.pop()
            visited_row[i] = False

    else:
        for j in range(n):
            if visited_col[j]:
                continue
            visited_col[j] = True
            picked_col.append(j)
            choose(row_cnt, col_cnt + 1)
            picked_col.pop()
            visited_col[j] = False




ans = 0
choose(1, 1)
print(ans)