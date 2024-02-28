MAX_INT = int(1e6)

a_move = [0] * (MAX_INT + 1)
b_move = [0] * (MAX_INT + 1)

n, m = map(int, input().split())

final_time = 0

current_time = 1

for _ in range(n):
    v, t = map(int, input().split())
    for c in range(current_time, current_time + t):
        a_move[c] = a_move[c - 1] + v
        current_time += 1

current_time = 1

for _ in range(m):
    v, t = map(int, input().split())
    for c in range(current_time, current_time + t):
        b_move[c] = b_move[c - 1] + v
        current_time += 1

cnt = 1
trophy = ''

for i in range(1, current_time):
    if a_move[i] > b_move[i]:
        if not trophy:
            prev_trophy = 'A'
        trophy = 'A'
    elif a_move[i] < b_move[i]:
        if not trophy:
            prev_trophy = 'B'
        trophy = 'B'
    else:
        if not trophy:
            prev_trophy = 'AB'
        trophy = 'AB'

    if prev_trophy != trophy:
        print(prev_trophy, trophy)
        cnt += 1
        prev_trophy = trophy

print(cnt)