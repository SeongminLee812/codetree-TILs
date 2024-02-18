m1, d1, m2, d2 = map(int, input().split())

days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

later = sum([days_of_month[i] for i in range(1, m2 + 1)]) + d2
faster = sum([days_of_month[i] for i in range(1, m1 + 1)]) + d1

print(later - faster)