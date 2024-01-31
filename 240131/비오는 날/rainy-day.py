n = int(input())

days = []

for _ in range(n):
    day, weekday, whether = input().split()
    if whether == 'Rain':
        days.append(day + ' ' + weekday + ' ' + whether)

def sorting(text: str) -> str:
    days, weekday, whether = text.split()
    y, m, d = days.split('-')
    return y, m, d

days.sort(key=sorting)
print(days[0])