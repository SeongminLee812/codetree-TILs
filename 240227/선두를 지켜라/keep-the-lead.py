MAX_INT = 1000000
a_move = [0] * (MAX_INT + 1)
b_move = [0] * (MAX_INT + 1)

n, m = map(int, input().split())

current_time = 0
total_time = 0
for _ in range(n):
    v, t = map(int, input().split())
    total_time += t
    for _ in range(t):
        current_time += 1
        a_move[current_time] = a_move[current_time - 1] + v

current_time = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        current_time += 1
        b_move[current_time] = b_move[current_time - 1] + v


cnt = 0
prev_first = ''
for current in range(1, total_time):
    if a_move[current] > b_move[current]:
        now_first = 'a'
        if not prev_first:
            prev_first = 'a'
    elif b_move[current] > a_move[current]:
        now_first = 'b'
        if not prev_first:
            prev_first = 'b'

    if prev_first and prev_first != now_first:
        cnt += 1
        prev_first = now_first

print(cnt)