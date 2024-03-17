n = int(input())
segments = []
for _ in range(n):
    start, end = map(int, input().split())
    segments.append((start, end))

def check(bool_list):
    for i in range(len(bool_list)):
        for j in range(i + 1, len(bool_list)):
            s1, e1 = bool_list[i]
            s2, e2 = bool_list[j]
            if (s1 <= s2 <= e1) or (s1 <= e2 <= e1) or (s2 <= s1 <= e2) or (s2 <= e1 <= e2):
                return False

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