def is_yoon(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

n = int(input())

if is_yoon(n):
    print('true')
else:
    print('false')