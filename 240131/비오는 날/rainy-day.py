n = int(input())

faster = '2101-01-01'
wkdy = ''
whe = ''

＃ 시간을 고려하여 작성
for _ in range(n):
    days, weekday, whether = input().split()
    if whether == 'Rain':
        y, m, d = days.split('-')
        prev_y, prev_m, prev_d = faster.split('-')
        if y < prev_y:
            faster, wkdy, whe = days, weekday, whether
        elif y == prev_y:
            if m < prev_m:
                faster, wkdy, whe = days, weekday, whether
            elif m == prev_m:
                if d < prev_d:
                    faster, wkdy, whe = days, weekday, whether

print(" ".join(map(str, [faster, wkdy, whe])))


＃ 시간을 고려하지 않고 편한 코드

# n = int(input())

# days = []

# for _ in range(n):
#     day, weekday, whether = input().split()
#     if whether == 'Rain':
#         days.append(day + ' ' + weekday + ' ' + whether)

# def sorting(text: str) -> str:
#     days, weekday, whether = text.split()
#     y, m, d = days.split('-')
#     return y, m, d

# days.sort(key=sorting)
# print(days[0])