n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

bomb_num = sorted(set(arr))

def check_bomb(num):
    bomb_cnt = 0
    for i in range(n - 1):
        if arr[i] == num:
            for j in range(i + 1, n):
                if arr[j] == num:
                    dist = j - i
                    if dist <= k:
                        bomb_cnt += 1
    return bomb_cnt

ans = 0
max_bomb_cnt = 0

for num in bomb_num:
    bomb_cnt = check_bomb(num)
    if bomb_cnt >= max_bomb_cnt:
        max_bomb_cnt = bomb_cnt
        ans = num

print(ans)