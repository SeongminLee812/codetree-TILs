n = int(input())
arr = list(map(int, input().split()))

sevens = []

for i in range(n):
    if arr[i] % 7 == 0:
        sevens.append(arr[i])

sums = sum(sevens)
mean = round(sums / len(sevens), 1)

print(len(sevens), sums, mean)