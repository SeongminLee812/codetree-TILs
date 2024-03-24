n, m = map(int, input().split())

ans = []

def choose(curr_num, start_num):
    if curr_num == m + 1:
        print(' '.join(map(str, ans)))
        return

    for i in range(start_num, n + 1):
        ans.append(i)
        choose(curr_num + 1, i + 1)
        ans.pop()


choose(1, 1)