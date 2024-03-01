import sys

n = int(input())
arr = list(map(int, list(input())))

def search_max_dist():
    # 시작점
    result_dist = 0
    result_index = 0
    for i in range(n - 1):
        # 끝점
        for j in range(i + 1, n):
            if arr[i] == 1 and arr[j] == 1:
                dist = j - i
                if dist > result_dist:
                    result_dist = dist
                    result_index = i
                break
    return result_dist, result_index

def search_min_dist():
    # 시작점
    result_dist = sys.maxsize
    result_index = 0
    for i in range(n - 1):
        # 끝점
        for j in range(i + 1, n):
            if arr[i] == 1 and arr[j] == 1:
                dist = j - i
                if dist < result_dist:
                    result_dist = dist
                    result_index = i
                break
    return result_dist

result_dist, result_index = search_max_dist()

arr[(result_index + result_dist) // 2] = 1
ans = search_min_dist()
print(ans)