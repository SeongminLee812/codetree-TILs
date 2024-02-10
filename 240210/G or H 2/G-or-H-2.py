n = int(input())
placed = [0] * 101
for _ in range(n):
    spot, alpha = input().split()
    spot = int(spot)
    placed[spot] = alpha

def check(people):
    count_G = 0
    count_H = 0
    for s in people:
        if s == 'G':
            count_G += 1
        elif s == 'H':
            count_H += 1
    if count_G and not count_H:
        return True
    if count_H and not count_G:
        return True
    if count_G == count_H:
        return True

    return False


ans = 0
for i in range(101):
    if placed[i]:
        for k in range(0, 101 - i): # k의 범위를 0~n - i만큼으로 정의한 후에 더해줌
            if placed[i + k]:
                if check(placed[i:i + k + 1]):
                    # print(placed[i:i + k + 1], 'k=', k)
                    size = k + 2
                    ans = max(ans, k)
                    # print(f'ans={ans}')
print(ans)