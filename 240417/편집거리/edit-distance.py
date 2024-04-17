import sys
INT_MIN = -sys.maxsize

A = " " + input()
B = " " + input()

memo = [
    [INT_MIN] * len(B)
    for _ in range(len(A))
]

# initialize
for i in range(len(A)):
    memo[i][0] = i
for j in range(len(B)):
    memo[0][j] = j

# memoization
def edit_distance(i, j):
    if memo[i][j] >= 0:
        return memo[i][j]

    if A[i] == B[j]:
        memo[i][j] = edit_distance(i - 1, j - 1)
    else:
        memo[i][j] = min(edit_distance(i - 1, j - 1), edit_distance(i - 1, j), edit_distance(i, j - 1)) + 1
    return memo[i][j]

print(edit_distance(len(A) - 1, len(B) - 1))