class Appointment:
    def __init__(self, scode, place, time):
        self.scode = scode
        self.place = place
        self.time = time

a = tuple(input().split())
ans = Appointment(*a)
print(f'secret code : {ans.scode}\nmeeting point : {ans.place}\ntime : {ans.time}')