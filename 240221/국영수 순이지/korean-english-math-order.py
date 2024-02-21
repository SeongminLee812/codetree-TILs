class Student():
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

arr.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for p in arr:
    print(p)