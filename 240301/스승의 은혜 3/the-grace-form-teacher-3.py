import copy

n, b = map(int, input().split())

class Student:
    def __init__(self, price, shipment):
        self.price = price
        self.shipment = shipment

    def __repr__(self):
        return f"Student(price: {self.price}, shipment: {self.shipment})"

students = []

for _ in range(n):
    p, s = map(int, input().split())
    students.append(Student(p, s))

ans = 0

# n개중 하나만 반값.
# 정렬 -> 싼 애들부터 채우면 됨
for i in range(n):
    now_p = copy.deepcopy(students)
    now_p[i].price //= 2

    now_p.sort(key=lambda x: x.price + x.shipment)
    remain_cost = b
    possible = 0

    for j in range(n):
        remain_cost -= now_p[j].price + now_p[j].shipment
        if remain_cost >= 0:
            possible += 1
        else:
            break
    ans = max(ans, possible)

print(ans)