n = int(input())

picked = []
visited = [False] * (n + 1)

def choose(cnt):
    # 정답의 cnt번째 수를 선택하는 함수
    if cnt == n + 1:
        print(' '.join(map(str, picked)))
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = True
        picked.append(i)
        
        choose(cnt + 1)

        picked.pop()
        visited[i] = False
    
choose(1)