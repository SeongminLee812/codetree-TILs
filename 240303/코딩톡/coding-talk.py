n, m, p = map(int, input().split())

# 메세지 별로 안읽어도 되는 사람을 기록/ 행 : 메세지, 열: 사람
can_unread =[
    [i for i in range(n)]
    for _ in range(m)
]

# result array / 1: 안읽을 가능성이 있는 사람, 0: 읽어야만 하는 사람
arr = [0] * n

# 메세지를 보낸 사람이 누구인지 체크
senders = [0] * m

# 각 메세지 별로 읽은 사람의 수를 기록하는 array
read_people = [0] * m

for i in range(m):
    person, nums = input().split()
    nums = int(nums)
    read_people[i] = nums
    person_num = ord(person) - ord('A')

    senders[i] = person_num
    # 안읽은 사람이 0인 경우 전부 제거
    if nums == 0:
        can_unread[i] = []

    # 이전 메세지에서 안읽어도 되는 사람 다 제거
    else:
        for prev_m in range(i + 1):
            try:
                can_unread[prev_m].remove(person_num)
            except:
                pass


for message_num in range(m):
    if message_num == 0:
        continue
    if read_people[message_num - 1] == read_people[message_num]:
        try:
            sender = senders[message_num - 1]
            # print(f'message: {message_num}, person: {sender}')
            can_unread[message_num].remove(sender) # 여기에 i - 1번째 메세지를 보낸 사람을 찾아서 제거
        except:
            pass

#
# for row in can_unread:
#     print(row)

# 정답 찾기
for person_num in can_unread[p - 1]:
    arr[person_num] = 1

for i in range(n):
    if arr[i]:
        char = chr(ord('A') + i)
        print(char, end=' ')