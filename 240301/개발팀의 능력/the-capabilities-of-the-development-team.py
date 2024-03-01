# 2명 뽑기
# 나머지 중 1명 뽑기
# 팀별 수치 계산
import sys

arr = list(map(int, input().split()))
all_sum = sum(arr)

ans = sys.maxsize
ok = False

for i in range(4):
    for j in range(i + 1, 5):
        first_team = arr[i] + arr[j]

        for k in range(5):
            if k == i or k == j:
                continue
            second_team = arr[k]
            third_team = all_sum - first_team - second_team

            score_list = [first_team, second_team, third_team]
            if len(set(score_list)) == 3:
                ok = True
                diff = max(score_list) - min(score_list)
                ans = min(ans, diff)

if ok:
    print(ans)
else:
    print(-1)