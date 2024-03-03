import sys

n, m, p = map(int, input().split())

messages =[
    list(input().split())
    for _ in range(m)
]

if messages[p - 1][1] == 0:
    sys.exit()

for i in range(n):
    person = chr(ord('A') + i)
    read = False

    for sender, unread_nums in messages:
        unread_nums = int(unread_nums)
        if unread_nums >= int(messages[p - 1][1]) and sender == person:
            read = True

    if not read:
        print(person, end=' ')