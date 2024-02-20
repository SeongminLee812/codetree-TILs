n, m = map(int, input().split())

A = list(map(int, input().split()))

def get_sum(a, b):
    print(sum(A[a - 1:b - 1 + 1]))

for _ in range(m):
    a, b = map(int, input().split())
    get_sum(a, b)