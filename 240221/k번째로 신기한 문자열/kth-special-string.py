n, k, t = input().split()

n, k = int(n), int(k)

includes = []
for _ in range(n):
    word = input()
    if word.find(t) == 0:
        includes.append(word)

includes.sort()
print(includes[k - 1])