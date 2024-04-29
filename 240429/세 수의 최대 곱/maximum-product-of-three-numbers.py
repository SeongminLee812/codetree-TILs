n = int(input())
arr = list(map(int, input().split()))

arr.sort()

pos_cnt = 0
zero_cnt = 0
neg_cnt = 0


for i in range(n):
    if arr[i] > 0:
        pos_cnt += 1
    elif arr[i] < 0:
        neg_cnt += 1
    else:
        zero_cnt += 1

candidate = []

if zero_cnt:
    candidate.append(0)
if neg_cnt >= 2 and pos_cnt >= 1:
    neg_two_and_pos_one = arr[0] * arr[1] * arr[-1]
    candidate.append(neg_two_and_pos_one)
candidate.append(arr[0] * arr[1] * arr[2])
candidate.append(arr[-1] * arr[-2] * arr[-3])

print(max(candidate))