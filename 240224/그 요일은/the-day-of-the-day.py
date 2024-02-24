days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekday_to_num = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 
                    'Fri': 4, 'Sat': 5, 'Sun': 6}

m1, d1, m2, d2 = map(int, input().split())
target = input()
target_num = weekday_to_num[target]

end_day = sum([days_of_month[m] for m in range(m2)]) + d2
start_day = sum([days_of_month[m] for m in range(m1)]) + d1

ans = 0
cur_day = 0
for i in range(start_day, end_day + 1):
    if cur_day == target_num:
        ans += 1
    cur_day = (cur_day + 1) % 7

print(ans)