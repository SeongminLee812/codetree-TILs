n = int(input())
a = list(map(int, input().split()))

limit = 1
for i in a:
    limit *= i

def go(num):
    if num == limit:
        print(limit)
        return limit

    baesu = True
    for i in a:
        if num % i != 0:
            baesu = False

    if baesu:
        print(num)
        return num
    else:
        go(num + MAX)

MAX = max(a)
go(max(a))