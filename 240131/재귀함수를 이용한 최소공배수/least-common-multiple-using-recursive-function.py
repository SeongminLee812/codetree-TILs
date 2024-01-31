n = int(input())
arr = [0] + list(map(int, input().split()))

# 두 수의 최대공약수
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

# 두 수의 최소공배수
def lcm(x, y):
    return (x * y) // gcd(x, y)

# index번째까지 인덱스의 숫자중에 가장 큰 값을 반환
def get_lcm_all(index):
    # 남은 원소가 1개라면 자기 자신이 답
    if index == 1:
        return arr[1]

    # 1번째 ~ indedx - 1번째 원소의 최소공배수를 구한 결과와
    # 현재 index 원소의 최소공배수를 구하여 반환
    return lcm(get_lcm_all(index - 1), arr[index])

# 모든 수의 최소공배수를 구함
print(get_lcm_all(n))