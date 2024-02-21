class Weather():
    def __init__(self, day, weekday, weather):
        self.day = day
        self.weekday = weekday
        self.weather = weather

    def __repr__(self):
        return f"{self.day} {self.weekday} {self.weather}"

n = int(input())
arr = [
    Weather(*tuple(input().split()))
    for _ in range(n)
]

min_idx = 0
for i in range(n):
    if arr[i].weather == 'Rain':
        if arr[i].day < arr[min_idx].day:
            min_idx = i

print(arr[min_idx])