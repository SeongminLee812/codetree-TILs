n = int(input())
segments = []
for _ in range(n):
    start, end = map(int, input().split())
    segments.append((start, end))

def check(bool_list):
    drawed = [False] * 1001

    for i in range(n):
        if bool_list[i]:
            start, end = segments[i]
            for x in range(start, end + 1):
                if drawed[x] != 0:
                    return False
                drawed[x] += 1

    return True


bool_list = []
ans = 0
def go(index):
    global ans
    if index == n + 1:
        if check(bool_list):
            cnt = sum(bool_list)
            ans = max(cnt, ans)
        return

    for i in range(2):
        bool_list.append(i)
        go(index + 1)
        bool_list.pop()

go(1)
print(ans)