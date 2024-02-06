n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

visited = [False] * 1001

def check(line):
    """ 사용 가능한 선분인지 체크하는 함수"""
    x1, x2 = line[0], line[1]
    for i in range(x1, x2 + 1):
        if visited[i]:
            return False
    return True

def use(line):
    """해당 선분을 사용하는 함수 : visited를 체크할 수 있게"""
    global visited, now
    x1, x2 = line[0], line[1]
    visited[x1:x2 + 1] = [True] * (x2 - x1 + 1)
    now.append((x1, x2))
    pass


now = []
ans = 0
def choose(index):
    global now, ans
    if index >= len(lines):
        ans = max(ans, len(now))
        return

    for i in range(index, len(lines)):
        if check(lines[i]):
            use(lines[i])
            choose(index + 1)
            now.pop()
        else:
            choose(index + 1)

choose(0)
print(ans)