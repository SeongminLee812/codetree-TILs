class Person():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f"{self.name} {self.height} {self.weight}"

n = int(input())
people = [
    Person(*tuple(input().split()))
    for _ in range(n)
]

people.sort(key=lambda x: x.height)

for p in people:
    print(p)