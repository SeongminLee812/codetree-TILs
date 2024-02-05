total = 0

def div(n):
    global total

    if n == 1:
        return

    total += 1

    if n % 2 == 0:
        return div(n // 2)
    else:
        return div(n // 3)

n = int(input())
div(n)
print(total)