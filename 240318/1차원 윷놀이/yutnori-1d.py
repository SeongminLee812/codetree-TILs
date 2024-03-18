# 배열 3개
## 각 턴에서 전진할 말의 배열
## input받은 n들의 배열
## 각 말 별로 지나간 칸을 합산하는 배열

n, m, k = map(int, input().split())
move_each_turn = list(map(int, input().split()))

def calc_score():
    total_pass = 0
    score_board = [1] * (k + 1)

    for i in range(n):
        score_board[knights[i]] += move_each_turn[i]
    for i in range(1, k + 1):
        if score_board[i] >= m:
            total_pass += 1
    return total_pass

def choose_knight(curr_index):
    global ans
    if curr_index == n + 1:
        score = calc_score()
        ans = max(ans, score)
        return

    for i in range(1, k + 1):
        knights.append(i)
        choose_knight(curr_index + 1)
        knights.pop()

knights = []
ans = 0

choose_knight(1)
print(ans)