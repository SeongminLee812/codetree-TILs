n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

picked = []

visited_row = [False] * n
visited_col = [False] * n


def choose(row_cnt):
    # picked의 cnt번째 수를 결정하는 함수
    global ans
    combi = 0

    if row_cnt == n + 1:
        ans = max(ans, sum(picked))
        combi += 1
        return

    for row in range(n):
        if visited_row[row]:
            continue
        visited_row[row] = True

        max_val = 0
        for col in range(n):
            if not visited_col[col] and arr[row][col] > max_val:
                return_col = col
                max_val = arr[row][col]
        picked.append(max_val)
        visited_col[return_col] = True

        choose(row_cnt + 1)
        picked.pop()
        visited_col[return_col] = False
        visited_row[row] = False




ans = 0
choose(1)
print(ans)