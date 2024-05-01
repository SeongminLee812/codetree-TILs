n = int(input())

counter = dict()
for _ in range(n):
    key = input()
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1

print(max(counter.values()))