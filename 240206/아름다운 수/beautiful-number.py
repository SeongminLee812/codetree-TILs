n = int(input())
ans = []
total = 0

def in_range(index, next_num, length):
    return index + next_num <= length

def string_check(index, repet_num, ans):
    ok = True
    if repet_num == 2:
        ok = ans[index] == ans[index + 1]
    elif repet_num == 3:
        ok = ans[index] == ans[index + 1] == ans[index + 2]
    elif repet_num == 4:
        ok = ans[index] == ans[index + 1] == ans[index + 2] == ans[index + 3]
    return ok

def check(ans):
    index = 0
    length = len(ans)
    while index < length:
        if ans[index] == 1:
            index += 1
        elif ans[index] == 2:
            if not in_range(index, 2, length):
                return False
            if not string_check(index, 2, ans):
                return False
            index += 2
        elif ans[index] == 3:
            if not in_range(index, 3, length):
                return False
            if not string_check(index, 3, ans):
                return False
            index += 3
        elif ans[index] == 4:
            if not in_range(index, 4, length):
                return False
            if not string_check(index, 4, ans):
                return False
            index += 4
    return True


def choose(index):
    global total, ans
    if index == n:
        print(ans)
        if check(ans):
            total += 1
            return
    if index > n:
        return
    for i in range(1, 5):
        ans.append(i)
        choose(index + 1)
        ans.pop()

choose(0)
print(total)