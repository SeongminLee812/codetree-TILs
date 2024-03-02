import copy

n = int(input())

prev_score = {'A': 0,
              'B': 0}

cnt = 0

for rounds in range(n):
    person, score = input().split()
    score = int(score)

    curr_score = copy.deepcopy(prev_score)
    curr_score[person] += score

    if prev_score['A'] >= prev_score['B'] and \
        curr_score['A'] < curr_score['B']:
        cnt += 1

    elif prev_score['A'] <= prev_score['B'] and\
        curr_score['A'] > curr_score['B']:
        cnt += 1

    elif prev_score['A'] != prev_score['B'] and\
        curr_score['A'] == curr_score['B']:
        cnt += 1

    prev_score = curr_score

print(cnt)