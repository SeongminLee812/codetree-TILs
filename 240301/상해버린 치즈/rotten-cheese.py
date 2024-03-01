from collections import defaultdict

n, m, d, s = map(int, input().split())

MAX_PEOPLE = n
MAX_CHEESE = m

# 먹은 시간 기록 배열 / 행: 사람, 열: 치즈, 레코드: 시간
eat_time_arr = [
    [0] * (MAX_CHEESE + 1)
    for _ in range(MAX_PEOPLE + 1)
]

# 아픈 사람 기록
sick_people = []

# 치즈를 먹은 사람의 수 카운트
cheese_cnt = defaultdict(set)

# 아픈 사람 시간 기록 배열 / 열: 사람, 레코드: 아픈 시간
sick_time_arr = [0] * (MAX_PEOPLE + 1)

for _ in range(d):
    person, cheese, when = map(int, input().split())
    eat_time_arr[person][cheese] = when
    cheese_cnt[cheese] = cheese_cnt[cheese].union({person})

for _ in range(s):
    person, when = map(int, input().split())
    sick_time_arr[person] = when
    sick_people.append(person)

cheese_candidate = []

for cheese_num in range(1, MAX_CHEESE + 1):
    possible = True
    for person_num in sick_people:
        # 안먹었거나, 이전에 먹은 경우 탈락
        if eat_time_arr[person_num][cheese_num] == 0 or eat_time_arr[person_num][cheese_num] >= sick_time_arr[person_num]:
            possible = False
    if possible:
        cheese_candidate.append(cheese_num)
    else:
        if cheese_num in cheese_candidate:
            cheese_candidate.remove(cheese_num)

ans = 0

for cheese_num in cheese_candidate:
    ans = max(ans, len(cheese_cnt[cheese_num]))

print(ans)