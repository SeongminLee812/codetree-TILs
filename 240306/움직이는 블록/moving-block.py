# 좋지 않은 선택
# 1. 이미 작은 수의 블럭을 다른 블럭으로 옮기는 것
# 따라서 이미 큰 수의 블럭을 가장 작은 곳으로 옯긴다.
# 최선의 선택 -> 가장 큰 놈을 옮기는 것
# 어떻게 ?
import sys


# 제일 큰놈에서 제일 작은 놈으로 옮기되 차이만큼 한번에 덜어줘야 복잡도를 줄일 수 있음
# 종료 조건 : 가장 큰 n이 다른 수와 동일해질 때까지

def find_min_max():
    max_val = 0
    min_val = sys.maxsize
    max_idx = 0
    min_idx = 0

    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    return min_val, min_idx, max_val, max_idx

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]


cnt = 0
for i in range(n):
    min_val, min_idx, max_val, max_idx = find_min_max()
    diff = max_val - min_val
    if diff == 0:
        break

    diff //= 2
    arr[max_idx] = max_val - diff
    arr[min_idx] = min_val + diff
    cnt += diff

print(cnt)