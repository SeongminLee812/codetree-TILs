class Student():
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def __repr__(self):
        return f'{self.height} {self.weight} {self.number}'

n = int(input())

results = []

for i in range(1, n + 1):
    h, w = map(int, input().split())
    results.append(Student(h, w, i))

results.sort(key=lambda x: (x.height, -x.weight))

for s in results:
    print(s)