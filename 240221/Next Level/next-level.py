class Character():
    def __init__(self, id='codetree', level='10'):
        self.id = id
        self.level = level

    def __repr__(self):
        return f"user {self.id} lv {self.level}"
    
id, lev = input().split()
c1 = Character()
print(c1)
c2 = Character(id, lev)
print(c2)