from collections import defaultdict

n, m = map(int, input().split())

arr = list(map(int, input().split()))
search_things = list(map(int, input().split()))

count_dict = defaultdict(int)

for i in range(n):
    count_dict[arr[i]] += 1


for search_thing in search_things:
    print(count_dict[search_thing], end=' ')