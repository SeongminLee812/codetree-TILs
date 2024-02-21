class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def __repr__(self):
        return f"""code : {self.code}\ncolor : {self.color}\nsecond : {self.second}"""

a = tuple(input().split())
bomb = Bomb(*a)
print(bomb)