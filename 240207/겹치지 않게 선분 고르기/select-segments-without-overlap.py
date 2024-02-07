n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

visited = [False] * 1001

# 체크로직 변경 필요!
def check(lines):
    """ 사용 가능한 선분인지 체크하는 함수"""
    visited = [False] * 1001
    for line in lines:
        x1, x2 = line
        for i in range(x1, x2 + 1):
            if visited[i]:
                return False
        visited[x1:x2 +1] = [True] * (x2 - x1 + 1)
    return True


ans = 0

def choose(index, now):
    global ans
    if index == len(lines):
        if check(now):
            ans = max(ans, len(now))
        return

    choose(index + 1, now + [lines[index]])
    choose(index + 1, now)

choose(0, [])
print(ans)