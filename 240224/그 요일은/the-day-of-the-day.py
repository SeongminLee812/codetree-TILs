days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
count_weekday = input()

# 요일 차이만큼 빼주기 위해서 요일 차이 미리 계산 
minus = 0
for i in range(len(weekdays)):
    if weekdays[i] == count_weekday:
        minus = i

end_day = sum([days_of_month[m] for m in range(m2)]) + d2
start_day = sum([days_of_month[m] for m in range(m1)]) + d1 + minus

elapsed_day = end_day - start_day

ans = 0
if elapsed_day >= minus:
    ans = elapsed_day // 7 + 1
elif elapsed_day < 0:
    ans = 0
else:
    ans = elapsed_day // 7

print(ans)