n = int(input())

def first(n):
    if n == 0:
        return
    first(n - 1)
    print(n, end=' ')

def second(n):
    if n == 0:
        return
    print(n, end=' ')
    second(n - 1)

first(n)
print()
second(n)