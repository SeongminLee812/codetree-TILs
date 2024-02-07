n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

# 체크로직 변경 필요!
def overlapped(line1, line2):
    (ax1, ax2), (bx1, bx2) = line1, line2

    return (ax1 <= bx1 and ax2 >= bx1) or (ax1 >= bx1 and bx2 >= ax1) or \
        (ax2 >= bx2 and ax1 <= bx2) or (ax2 <= bx2 and bx1 <= ax2)

def check():
    """ 사용 가능한 선분인지 체크하는 함수"""
    for i, line1 in enumerate(selected):
        for j, line2 in enumerate(selected):
            if i > j and overlapped(line1, line2):
                return False
    return True

ans = 0
selected = []

def choose(index):
    global ans
    if index == len(lines):
        if check():
            ans = max(ans, len(selected))
        return

    selected.append(lines[index])
    choose(index + 1)
    selected.pop()
    choose(index + 1)

choose(0)
print(ans)