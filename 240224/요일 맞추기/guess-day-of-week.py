days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = dict(zip([i for i in range(7)], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']))

m1, d1, m2, d2 = map(int, input().split())

end_day = sum([days_of_month[m] for m in range(m2)]) + d2
start_day = sum([days_of_month[m] for m in range(m1)]) + d1

elapsed_day = end_day - start_day

ans = weekday[elapsed_day % 7]
print(ans)