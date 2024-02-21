from functools import cmp_to_key

class Student():
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def __repr__(self):
        return f"{self.height} {self.weight} {self.number}"

def compare(x, y):
    if x.height > y.height:
        return -1
    if x.height < y.height:
        return 1
    if x.weight > y.weight:
        return -1
    if x.weight < y.weight:
        return 1
    if x.number < y.number:
        return -1
    if x.number > y.number:
        return 1
    return 0

n = int(input())
students = []

for i in range(1, n + 1):
    h, w = map(int, input().split())
    students.append(Student(h, w, i))

students.sort(key=cmp_to_key(compare))

for s in students:
    print(s)