m, d = map(int, input().split())

def is_possible(month, day):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12:
        return False

    if day <= days[month]:
        return True
    else:
        return False

if is_possible(m, d):
    print('Yes')
else:
    print('No')