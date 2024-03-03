arr = list(map(int, input().split()))

longest_term = 0

for i in range(len(arr)):
    if i == 0:
        continue
    term = arr[i] - arr[i - 1]
    longest_term = max(longest_term, term)

if longest_term == 1:
    print(0)
elif longest_term == 2:
    print(1)
else:
    print(longest_term - 1)