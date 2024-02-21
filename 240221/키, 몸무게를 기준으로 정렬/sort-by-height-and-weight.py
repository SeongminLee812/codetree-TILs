class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

    def __repr__(self):
        return f'{self.name} {self.height} {self.weight}'

n = int(input())
people = [
    Person(*tuple(input().split()))
    for _ in range(n)
]

for p in sorted(people, key=lambda x: (x.height, -x.weight)):
    print(p)