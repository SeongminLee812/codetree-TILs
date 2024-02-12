import copy

n = int(input())
h = [int(input()) for _ in range(n)]

def count_ice(array):
    count = 0
    for i in range(len(array) - 1):
        if (array[i] > 0 and array[i + 1] == 0) or (i + 1 == len(array) - 1 and array[i + 1] > 0):
            count += 1
    return count

ans = 0

final_h = []
final_cnt = 0

for i in range(0, max(h) + 1):
    height = i
    now_h = copy.deepcopy(h)
    for j in range(n):
        now_h[j] -= height
        if now_h[j] < 0:
            now_h[j] = 0
    cnt = count_ice(now_h)

    if cnt > ans:
        final_h = now_h
        ans = cnt

print(ans)