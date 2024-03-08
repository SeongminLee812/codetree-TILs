from collections import deque

n = int(input())

segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

small_q = sorted(segments, key=lambda x: (-x[0], x[1] - x[0]))
large_q = sorted(segments, key=lambda x: (x[1], x[1] - x[0]))


small_q.pop()
list1 = []
for i in small_q:
    list1.append(i[0])
    list1.append(i[1])

length1 = max(list1) - min(list1)

large_q.pop()
list2 = []
for i in large_q:
    list2.append(i[0])
    list2.append(i[1])
length2 = max(list2) - min(list2)

print(min(length1, length2))