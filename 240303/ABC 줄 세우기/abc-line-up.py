n = int(input())
arr = input().split()

incorrect_pos = 0

for i in range(n):
    correct = chr(i + ord('A'))
    if arr[i] != correct:
        incorrect_pos += 1

if incorrect_pos == 0:
    print(0)
else:
    print(incorrect_pos - 1)