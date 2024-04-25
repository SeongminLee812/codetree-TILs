n = int(input())

class Student():
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def __repr__(self):
        return str(self.height) + ' ' + str(self.weight) + ' ' + str(self.number)

arr = []
for i in range(1, n + 1):
    h, w = map(int, input().split())
    arr.append(Student(h, w, i))

arr.sort(key=lambda x: (x.height, -x.weight))
for i in range(n):
    print(arr[i])