class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

    def __repr__(self):
        return f"{self.height} {self.weight} {self.num}"

n = int(input())
students = []

for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i + 1))

students.sort(key=lambda x: (x.height, -x.weight))

for s in students:
    print(s)