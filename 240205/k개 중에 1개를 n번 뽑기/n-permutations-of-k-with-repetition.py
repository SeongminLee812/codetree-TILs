k, n = map(int, input().split())
ans = []

def choose(index):
    global ans
    if index == n:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, k + 1):
        ans.append(i)
        choose(index + 1)
        ans.pop()

choose(0)