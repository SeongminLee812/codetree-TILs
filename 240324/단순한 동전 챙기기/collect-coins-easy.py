import sys

n = int(input())

arr = [
    list(input())
    for _ in range(n)
]

coins = []
start = ''
end = ''

for i in range(n):
    for j in range(n):
        if arr[i][j].isdigit():
            coins.append((int(arr[i][j]), i, j))
        elif arr[i][j] == 'S':
            start = (0, i, j) # coins와 형식을 맞추기 위해 제일 앞 원소를 의미없는 0을 넣어줌
        elif arr[i][j] == 'E':
            end = (0, i, j)
coins.sort(key=lambda x: x[0])
coin_cnt = len(coins)


def get_dist(start_point, end_point):
    diff_x = abs(end_point[1] - start_point[1])
    diff_y = abs(end_point[2] - start_point[2])
    return diff_x + diff_y

def find_combi(curr_index, cnt, dist, last_index):
    '''
    전체 동전 중 curr_index 번째 함수를 선택할 지 선택하지 않을 지 결정하는 함수
    동전의 개수가 3이 되거나, curr_index가 동전의 개수를 초과하면 종료
    종료 시 end와의 거리를 합쳐서 출력함
    오름차순으로 골라야하므로 직전에 선택한 동전의 index 다음 값만 선택에 고려함.
    :param curr_index: 선택할 지 말지 고르는 동전의 index
    :param cnt: 몇개의 동전을 선택하였는지
    :param dist: 현재까지의 이동거리
    :param last_index: 직전에 선택한 동전의 index_
    :return:
    '''
    global ans

    if cnt == 3:
        dist = dist + get_dist(coins[last_index], end)
        ans = min(ans, dist)
        return
    if curr_index == coin_cnt + 1:
        return

    for i in range(last_index + 1, coin_cnt):
        # 선택
        diff = get_dist(coins[last_index], coins[i])
        find_combi(curr_index=curr_index + 1,
                   cnt=cnt + 1,
                   dist=dist + diff,
                   last_index=i)
        # 선택하지 않음
        find_combi(curr_index + 1, cnt, dist, i)

# 도달할 수 없는 경우 예외처리
if coin_cnt < 3:
    print(-1)
    sys.exit()

ans = sys.maxsize

# 시작 코인 설정
for i in range(0, coin_cnt - 2):
    dist = get_dist(start, coins[i])
    find_combi(0, 1, dist, i)

print(ans)