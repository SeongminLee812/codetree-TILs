n = int(input())

first_cnt = 0
second_cnt = 0

for _ in range(n):
    num1, num2 = map(int, input().split())
    if ((num1 - num2) + 3) % 3 == 1:
        first_cnt += 1
    elif ((num2 - num1) + 3) % 3 == 1:
        second_cnt += 1

print(max(first_cnt, second_cnt))