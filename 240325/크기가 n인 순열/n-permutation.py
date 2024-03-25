n = int(input())

ans = []
visited = [False] * (n + 1)

def choose(curr_num):
    # ans의 curr_num번째 숫자를 선택하는 함수
    if curr_num == n + 1:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        ans.append(i)

        choose(curr_num + 1)

        ans.pop()
        visited[i] = False

choose(1)