import copy

n = int(input())

def who_first(scores):
    A, B, C = scores['A'], scores['B'], scores['C']
    return_val = 0

    """
    A만 올라간 경우 1
    B만 올라간 경우 2
    C만 올라간 경우 4
    AB 올라간 경우 3
    AC 올라간 경우 5
    BC 올라간 경우 6
    ABC 올라간 경우 7 
    """
    max_val = max(A, B, C)
    if max_val == A:
        return_val += 1
    if max_val == B:
        return_val += 2
    if max_val == C:
        return_val += 4

    return return_val

score_dict = {'A': 0, 'B': 0, 'C': 0}
prev_dict = {'A': 0, 'B': 0, 'C': 0}

cnt = 0

for _ in range(n):
    man, score = input().split()
    score = int(score)

    score_dict[man] += score
    if who_first(prev_dict) != who_first(score_dict):
        cnt += 1
    prev_dict['A'], prev_dict['B'], prev_dict['C'] = score_dict['A'], score_dict['B'], score_dict['C']

print(cnt)