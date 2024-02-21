class Spy:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

    def __repr__(self):
        return f'{self.code_name} {self.score}'

spies = [
    Spy(*tuple(input().split()))
    for _ in range(5)
]

print(min(spies, key=lambda x: int(x.score)))