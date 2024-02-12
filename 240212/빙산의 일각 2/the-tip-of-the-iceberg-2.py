import copy

n = int(input())
h = [int(input()) for _ in range(n)]

def count_ice(array):
    count = 0
    i = 0
    j = len(array) - 1
    if len(array) % 2 != 0: # 홀수인경우 패딩을 붙임
        array += [0]
        j += 1
    while i < j:
        if array[i] > 0 and array[i + 1] == 0:
            count += 1
        if array[j] > 0 and array[j - 1] == 0:
            count += 1
        i += 1
        j -= 1
    return count

ans = 0

for i in range(0, max(h) + 1):
    height = i
    now_h = copy.deepcopy(h)
    for j in range(n):
        now_h[j] -= height
        if now_h[j] < 0:
            now_h[j] = 0
    cnt = count_ice(now_h)
    # print(now_h, f'\tcount={cnt}')
    ans = max(ans, cnt)

print(ans)