k, n = map(int, input().split())

rankings = [[] for _ in range(n + 1)]

records = []
for _ in range(k):
    records.append(list(map(int, input().split())))

ans = 0

for first in range(1, n + 1):
    first_beater = []
    for second in range(1, n + 1):
        if first == second:
            continue
        first_ranking = 0
        second_ranking = 0
        first_win = True
        for record in records:
            for rank, person in enumerate(record):
                if first == person:
                    first_ranking = rank
                if second == person:
                    second_ranking = rank
            if second_ranking < first_ranking:
                first_win = False
        if first_win:
            first_beater.append(second)
            ans += 1

    rankings[first].extend(first_beater)
# print(rankings)

print(ans)