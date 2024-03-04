n = int(input())
score_dict = {'A': 0, 'B': 0}

cnt = 0

for _ in range(n):
    man, score = input().split()
    score = int(score)

    if score_dict['A'] > score_dict['B']:
        score_dict[man] += score
        if score_dict['A'] <= score_dict['B']:
            cnt += 1
    elif score_dict['A'] < score_dict['B']:
        score_dict[man] += score
        if score_dict['A'] >= score_dict['B']:
            cnt += 1
    else:
        score_dict[man] += score
        if score_dict['A'] != score_dict['B']:
            cnt += 1

print(cnt)