import sys
from functools import reduce

MIN_INT = -sys.maxsize
MAX_INT = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

neg = [MAX_INT, MAX_INT, MAX_INT]
pos = [MIN_INT, MIN_INT, MIN_INT]
is_zeros_in = False

pos_cnt = 0
neg_cnt = 0

small_abs = []

for i in range(n):
    if arr[i] < 0:
        if arr[i] < max(neg):
            neg.remove(max(neg))
            neg.append(arr[i])
        neg_cnt += 1
    elif arr[i] > 0:
        if arr[i] > min(pos):
            pos.remove(min(pos))
            pos.append(arr[i])
        pos_cnt += 1
    else:
        is_zeros_in = True


#
# print(neg)
# print(pos)
# print(is_zeros_in, pos_cnt, neg_cnt)

candidate = []

if is_zeros_in:
    candidate.append(0)

if pos_cnt >= 3:
    val = reduce(lambda x, y: x * y, pos)
    candidate.append(val)

# 양수 1개 이상, 음수 2개 이상인 경우
if pos_cnt >= 1 and neg_cnt >= 2:
    values = sorted(neg)[0:2] + [max(pos)]
    val = reduce(lambda x, y: x * y, values)
    candidate.append(val)


# 양수가 0개인 경우, 0도 없는 경우 -> 절대값이 가장 작은 음수 3개만 사용 -> neg의 곱
if pos_cnt <= 0 and not is_zeros_in:
    values = sorted(arr, key=abs)[:3]
    val = reduce(lambda x, y: x * y, values)
    candidate.append(val)

# 음수1개 양수 2개
if pos_cnt <= 2 and neg_cnt <= 1 and not is_zeros_in:
    values = [i for i in pos + neg if i != MIN_INT or i != MAX_INT]
    # print(len(values))
    val = reduce(lambda x, y: x * y, values)
    candidate(val)

print(max(candidate))