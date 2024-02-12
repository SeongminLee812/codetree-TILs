n = int(input())
string = input()

max_len = 0
for window_size in range(1, n // 2 + 1):
    ok = False
    for index in range(n):
        query = string[index:index + window_size]
        # print(f'window_size={window_size}, index={index}, query={query}')

        for search_index in range(index + window_size, n - window_size + 1):
            if string[search_index:search_index + window_size] == query:
                ok = True
                # print('!!!!!!!!!!!!!!!!!check!!!!!!!!!!!!!!!!!!!!!')
                # print(f'window_size={window_size}, index={index}, query={query}')
                # print(f'index={search_index}, search_string={string[search_index:search_index + window_size]}')
                break
        if ok:
            max_len = window_size
            break

print(max_len + 1)