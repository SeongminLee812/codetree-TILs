n = int(input())
a = list(map(int, input().split()))

MAX = 1
for i in a:
    MAX *= i

def go(num):
    if num == MAX:
        print(MAX)
        return MAX

    baesu = True
    for i in a:
        if num % i != 0:
            baesu = False

    if baesu:
        print(num)
        return num
    else:
        go(num + 1)

go(max(a))