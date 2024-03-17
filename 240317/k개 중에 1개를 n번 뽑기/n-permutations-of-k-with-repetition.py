k, n = map(int, input().split())

ans = []

def print_answer():
    print(' '.join(map(str, ans)))

def choose(index):
    if index == n + 1:
        print_answer()
        return

    for i in range(1, k + 1):
        ans.append(i)
        choose(index + 1)
        ans.pop()

choose(1)