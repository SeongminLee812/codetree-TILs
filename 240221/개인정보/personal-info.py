class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

    def __repr__(self):
        return f'{self.name} {self.height} {self.weight:.1f}'

people = [
    Person(*tuple(input().split()))
    for _ in range(5)
]

print('name')
for p in sorted(people, key=lambda x: x.name):
    print(p)

print()
print('height')
for p in sorted(people, key=lambda x: -x.height):
    print(p)