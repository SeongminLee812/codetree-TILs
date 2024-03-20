# 배열 3개
## 각 턴에서 전진할 말의 배열
## input받은 n들의 배열
## 각 말 별로 지나간 칸을 합산하는 배열

n, m, k = map(int, input().split())
move_each_turn = list(map(int, input().split()))

def calc_score():
    total_pass = 0
    for i in range(k):
        if score_board[i] <= 1:
            total_pass += 1
    return total_pass


def choose_knight(curr_index):
    global ans
    if curr_index == n:
        score = calc_score()
        ans = max(ans, score)
        return

    for i in range(k):
        if score_board[i] > 0:
            knights.append(i)
            score_board[i] = score_board[i] - move_each_turn[curr_index]
            choose_knight(curr_index + 1)
            score_board[i] += move_each_turn[curr_index]
            knights.pop()
        else:
            choose_knight(curr_index + 1)

knights = []
ans = 0
score_board = [m] * k

choose_knight(0)
print(ans)