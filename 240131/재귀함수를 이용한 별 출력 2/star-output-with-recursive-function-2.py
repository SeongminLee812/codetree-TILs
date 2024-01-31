n = int(input())

def go(line, star):
    print('* ' * star)
    if line == n * 2:
        return

    if line < n:
        go(line + 1, star - 1)
    elif line == n:
        go(line + 1, star)
    else:
        go(line + 1, star + 1)

go(1, n)