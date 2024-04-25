# 1. 몇일 지났는 지 확인
m1, d1, m2, d2 = map(int, input().split())
target = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_date = 0
end_date = 0

for i in range(1, m1):
    start_date += month[i]
start_date += d1
for i in range(1, m2):
    end_date += month[i]
end_date += d2
diff = end_date - start_date

day_dict = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
day_dict = dict(zip(day_dict.values(), day_dict.keys()))

ans = 0
cur_day = 0
for _ in range(diff + 1):
    if day_dict[cur_day] == target:
        ans += 1
    cur_day = (cur_day + 1) % 7

print(ans)