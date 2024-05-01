from collections import Counter

n, m = map(int, input().split())

arr = list(map(int, input().split()))
search_things = list(map(int, input().split()))

count_dict = Counter(arr)

for search_thing in search_things:
    print(count_dict[search_thing], end=' ')