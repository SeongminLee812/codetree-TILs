n = int(input())

def print_star(start, step):
    if start == n:
        print(' ' * step + '*' * start)
        return

    print(' ' * step + '*' * start)
    print_star(start + 2, step + 1)
    print(' ' * step + '*' * start)

print_star(1, 0)