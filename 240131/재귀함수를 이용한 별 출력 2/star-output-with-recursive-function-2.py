n = int(input())


def go(line, star):
    print('*' * star)
    if line == n * 2 - 1:
        return

    if line < n:
        go(line + 1, star - 1)
    else:
        go(line + 1, star + 1)

go(1, n)