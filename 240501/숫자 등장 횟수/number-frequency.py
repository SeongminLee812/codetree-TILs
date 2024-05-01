n, m = map(int, input().split())

arr = list(map(int, input().split()))
search_things = list(map(int, input().split()))

count_dict = dict()

for search_thing in search_things:
    count_dict[search_thing] = 0
    for target in arr:
        if target == search_thing:
            count_dict[search_thing] += 1

for search_thing in search_things:
    print(count_dict[search_thing], end=' ')