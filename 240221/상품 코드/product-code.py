class Product:
    def __init__(self, name='codetree', code='50'):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"product {self.code} is {self.name}"

name, code =input().split()
p1 = Product()
p2 = Product(name, code)
print(p1)
print(p2)