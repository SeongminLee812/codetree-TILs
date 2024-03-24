n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

score_board = [1] * k
def calc_score():
    cnt = 0
    for i in range(k):
        if score_board[i] >= m:
            cnt += 1
    return cnt


ans = 0

def choose(curr_num):
    global ans
    ans = max(calc_score(), ans)
    if curr_num == n:
        cnt = calc_score()
        ans = max(cnt, ans)
        return

    for i in range(k):
        if score_board[i] >= m:
            continue
        score_board[i] += arr[curr_num]
        choose(curr_num + 1)
        score_board[i] -= arr[curr_num]

choose(0)
print(ans)