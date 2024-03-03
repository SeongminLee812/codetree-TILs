n = int(input())
arr = input().split()

def move(original_array, current_pos, correct_pos) -> list:
    """
    임의의 알파벳을 제자리로 돌려놓고, 나머지 알파벳은 한칸씩 밀어내기
    :param original_array: 이동 전 array
    :param current_pos: 이동 시킬 알파벳의 현재 위치 인덱스
    :param correct_pos: 이동해야할 위치 인덱스
    :return:
    """
    new_array = [0] * n
    # 새로운 array에 이동시킬 원소 먼저 자리 잡기
    new_array[correct_pos] = original_array[current_pos]

    original_pos = 0
    new_pos = 0
    while True:
        if new_pos == current_pos:
            original_pos += 1
        elif new_pos == correct_pos:
            new_pos += 1

        if new_pos >= n:
            break

        new_array[new_pos] = original_array[original_pos]
        original_pos += 1
        new_pos += 1

    return new_array

def search():
    """
    전체 우리의 array를 탐색하면서 있어야할 제자리와 가장 먼 거리에 있는 알파벳의 위치 인덱스 및 이동이 필요한 횟수 반환
    :return: 위치 인덱스, 이동이 필요한 횟수
    """
    longest_dist = 0
    farthest_pos = 0
    final_pos = 0
    for i in range(n):
        correct_pos = ord(arr[i]) - ord('A')
        dist = abs(i - correct_pos)
        if dist > longest_dist:
            longest_dist = dist
            farthest_pos = i
            final_pos = correct_pos

    return farthest_pos, longest_dist, final_pos

# 제자리 수 구하기
def count_incorrect():
    cnt = 0
    for i in range(n):
        if chr(ord('A') + i) != arr[i]:
            cnt += 1
    return cnt


ans = 0
while count_incorrect():
    farthest_pos, longest_dist, correct_pos = search()
    ans += longest_dist
    # print(f'orig_pos: {farthest_pos}, longest: {longest_dist}, cor: {correct_pos}')
    arr = move(arr, farthest_pos, correct_pos)
    # print(arr)

print(ans)