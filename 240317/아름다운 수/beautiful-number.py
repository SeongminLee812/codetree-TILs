n = int(input())

def is_beautiful(answer_list):
    idx = 0
    length = len(answer_list)
    while idx < length:
        num = answer_list[idx]
        if idx + num > length:
            return False
        for i in range(idx, idx + num):
            if answer_list[i] != num:
                return False
        idx += num
    return True


def choose(index):
    global cnt
    if index == n + 1:
        if is_beautiful(answer_list=ans):
            cnt += 1
        return

    for i in range(1, 5):
        ans.append(i)
        choose(index + 1)
        ans.pop()

ans = []
cnt = 0

choose(1)
print(cnt)