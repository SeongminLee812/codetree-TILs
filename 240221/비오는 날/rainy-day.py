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

sorted_arr = sorted(arr, key=lambda x: x.day)

for w in sorted_arr:
    if w.weather == 'Rain':
        print(w)
        break