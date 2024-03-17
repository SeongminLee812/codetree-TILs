n = int(input())
segments = []
for _ in range(n):
    start, end = map(int, input().split())
    segments.append((start, end))

def check(bool_list):
    drawed = [False] * 1001

    for i in range(len(bool_list)):
        start, end = bool_list[i]
        for x in range(start, end + 1):
            if drawed[x] != 0:
                return False
            drawed[x] += 1

    return True


bool_list = []
ans = 0
def go(cnt):
    global ans
    if cnt == n:
        if check(bool_list):
            ans = max(ans, len(bool_list))
        return

    bool_list.append(segments[cnt])
    go(cnt + 1)
    bool_list.pop()

    go(cnt + 1)

go(0)
print(ans)