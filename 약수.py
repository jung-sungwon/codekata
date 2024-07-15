# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서,
# 약수의 개수가 짝수인 수는 더하고,
# 약수의 개수가 홀수인 수는 뺀 수를
# return 하도록 solution 함수를 완성해주세요.

# left	right	result
# 13	17      43
# 24	27	    52
# ==============================
# 아래는 약수 의 개수를 구하기 위한 함수이다
def divisor(n):
    count = 0
    # 임의 의 숫자를 1부터 돌면서 1~n 으로 나누어 나머지가 0 인수를 찾는다
    for i in range(1, n+1):
        if n % i == 0:
            # 나머지가 0 인수를 찾았으면(약수) 카운트에 1을 더해준다
            count += 1
    return count

# 아래는 약수가 짝수 인지 홀수인지 확인하여 더해주거나 빼주는 함수이다
def solution(left, right):
    total = 0
    # left 에서 right 까지 임의 의 수를 
    for num in range(left, right+1):
        # 약수를 확인하는 함수에 넣어 약수의 갯수가 짝수 인지 확인하고
        if divisor(num) % 2 == 0:
            # 짝수 면 토탈에 더해준다
            total += num
        else:
            # 홀수라면 토탈에서 빼준다
            total -= num
    return total


left = 13
right = 17
print(solution(left, right))
