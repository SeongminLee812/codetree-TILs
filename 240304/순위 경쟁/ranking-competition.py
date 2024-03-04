import copy

n = int(input())

def who_first(scores):
    A, B, C = scores['A'], scores['B'], scores['C']

    # 단독 1등
    if A > B and A > C:
        return 'A'
    elif B > C and B > A:
        return 'B'
    elif C > A and C > B:
        return 'C'
    # 두명이 1등
    elif A > B and A == C:
        return 'AC'
    elif B > A and B == C:
        return 'BC'
    elif A > C and A == B:
        return 'AB'
    # 세명이 1등
    elif A == B == C:
        return 'ABC'

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