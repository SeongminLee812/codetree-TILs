n = int(input())
arr = []
for _ in range(n):
    num, strike, ball = map(int, input().split())
    arr.append((num, strike, ball))

def check(my_num: str, target: str, t_strike: int, t_ball: int):
    strike = 0
    ball = 0
    for i in range(3):
        if my_num[i] == target[i]:
            strike += 1
        elif my_num[i] == target[i - 1] or my_num[i] == target[i - 2]:
            ball += 1
    if strike == t_strike and ball == t_ball:
        return True
    else:
        return False


ans = 0
for i in range(1, 10):
    for j in range(1 , 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                ok = True
                my_num = str(i) + str(j) + str(k)
                for target, strike, ball in arr:
                    if not check(my_num, str(target), strike, ball):
                        ok = False
                if ok:
                    # print(my_num) 
                    ans += 1
print(ans)