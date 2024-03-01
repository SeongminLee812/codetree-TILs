n = int(input())
strings = input()

def is_continous(start, search_space):
    print('is_continous')
    c_cnt = 0
    for j in range(start, start + search_space - 1):
        if ord(strings[j]) < ord(strings[j + 1]):
            print('continous!')
            c_cnt += 1
    if c_cnt == search_space - 1:
        return True
    return False


ans = 1

for search_space in range(2, n): # 연속 구간 탐색
    ok = False
    for i in range(0, n - search_space + 1): # 시작지점 고정
        for j in range(i + 1, n - search_space + 1): # 다른 지점을 탐색하면서 동일한 게 있는 지
            if i == j:
                continue
            if strings[i:i + search_space] == strings[j:j + search_space]:
                ok=True
                break
    if not ok:
        ans = search_space
        break

print(ans)