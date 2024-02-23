m1, d1, m2, d2 = map(int, input().split())

day_by_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

end_day = sum(day_by_month[:m2]) + d2
start_day = sum(day_by_month[:m1]) + d1
print(end_day - start_day + 1)