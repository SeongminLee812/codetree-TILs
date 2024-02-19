def check(A_short, B):
    if len(A_short) < len(B):
        return False
    for i in range(len(B)):
        if A_short[i] != B[i]:
            return False
    return True

def is_continuous(A, B):
    for j in range(n1 - n2 + 1):
        if A[j] == B[0]:
            if A[j: j + n2] == B:
                return True
    return False

n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if is_continuous(A, B):
    print('Yes')
else:
    print('No')