from functools import cmp_to_key

def compare(x, y):
    if sum([x.kor, x.eng, x.math]) < sum([y.kor, y.eng, y.math]):
        return -1
    if sum([x.kor, x.eng, x.math]) > sum([y.kor, y.eng, y.math]):
        return 1
    return 0

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

    def __repr__(self):
        return f"{self.name} {self.kor} {self.eng} {self.math}"

n = int(input())
arr = [
    Student(*tuple(input().split()))
    for _ in range(n)
]

arr.sort(key = cmp_to_key(compare))

for s in arr:
    print(s)