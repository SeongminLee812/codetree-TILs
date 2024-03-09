n = int(input())

arr = list(map(int, input().split()))

odd = 0
even = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

turn = 0
cnt = 0
while True:
    if turn == 0: # 짝수 턴일 때
        if even:
            even -= 1
        else:
            if odd >= 2: # 홀수가 2개 이상 남아있을 때
                odd -= 2
            else: # 홀수가 2개 이하로 남아있는 경우 while문 탈출
                break

    else: # 홀수 턴일 때
        if odd:
            odd -= 1
        else:
            break

    turn = (turn + 1) % 2
    cnt += 1

if odd: # 홀수 개수가 남아있는 경우 / 짝수 턴인 경우만 홀수가 남아있을 수 있음
    cnt -= 1

print(cnt)