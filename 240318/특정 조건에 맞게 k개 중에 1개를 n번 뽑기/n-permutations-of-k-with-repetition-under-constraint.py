k, n = map(int, input().split())

ans = []
def choose(curr_index):
    if curr_index == n + 1:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, k + 1):
        if curr_index > 2 and ans[-1] == ans[-2] == i:
            continue
        ans.append(i)
        choose(curr_index + 1)
        ans.pop()

choose(1)