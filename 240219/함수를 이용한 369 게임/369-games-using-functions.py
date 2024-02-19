def is_369(num):
    for s in str(num):
        if s in ['3', '6', '9']:
            return True
    return False

def is_check(num):
    if num % 3 == 0 or is_369(num):
        return True

def total(a, b):
    result = 0
    for i in range(a, b + 1):
        if is_check(i):
            result += 1
    return result

a, b = map(int, input().split())
print(total(a, b))