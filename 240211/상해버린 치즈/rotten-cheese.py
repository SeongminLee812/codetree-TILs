from collections import defaultdict

n, m, d, s = map(int, input().split())

# 나중에 탐색할 배열 : 각 사람마다 (먹은 시간, 먹은 치즈) 기록
search_space = [[] for _ in range(n + 1)]
# 치즈를 먹은 사람의 수를 기록
person_per_cheese = defaultdict(int)
# person_per_cheese를 기록할 때 한 사람이 치즈를 두번 먹었을 때 추가적인 메모가 되지 않도록 체크
person_already_eat = [[] for _ in range(n + 1)]



for _ in range(d):
    p, m, t = map(int, input().split())
    search_space[p].append((t, m))
    if m not in person_already_eat[p]:
        person_already_eat[p].append(m)
        person_per_cheese[m] += 1


candidate = []

for i in range(s):
    person, sick_time = map(int, input().split())
    people_cheese = []
    if i == 0: # first time
        for j in range(len(search_space[person])):
            eat_time, cheese = search_space[person][j]
            if eat_time < sick_time:
                people_cheese.append(cheese)
        candidate += people_cheese
    else:
        for j in range(len(search_space[person])):
            eat_time, cheese = search_space[person][j]
            if eat_time < sick_time:
                people_cheese.append(cheese)
        candidate = [c for c in people_cheese if c in candidate]


ans = 0
for c in candidate:
    ans = max(ans, person_per_cheese[c])
print(ans)