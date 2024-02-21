class Person():
    def __init__(self, name, postcode, city):
        self.name = name
        self.postcode = postcode
        self.city = city

    def __repr__(self):
        return f"name {self.name}\naddr {self.postcode}\ncity {self.city}"

n = int(input())
people = [
    Person(*tuple(input().split()))
    for _ in range(n)
]

max_idx = 0
for i in range(n):
    if people[i].name > people[max_idx].name:
        max_idx = i

print(people[max_idx])