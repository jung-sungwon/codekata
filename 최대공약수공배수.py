# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수,
# solution을 완성해 보세요. 배열의 맨 앞에 최대공약수,
# 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3,
# 최소공배수는 12이므로 solution(3, 12)는
# [3, 12]를 반환해야 합니다.

def solution(n, m):           # 함수 정의
    answer = []               # 답을 넣어줄 빈 리스트 생성

    n_ = []                   # n리스트에 약수를 넣어줄 리스트 생성
    for i in range(1, n+1):   # 1~n 까지의 수를 꺼내
        if n % i == 0:        # n 을 나눠주고 나머지가 0 이면 약수 이기 때문에
            n_.append(i)      # 리스트에 넣어준다

    m_ = []                   # m 도 동일하게 약수를 구하여 넣어준다
    for i in range(1, m+1):
        if m % i == 0:
            m_.append(i)

    set_n = set(n_)           # 두 약수의 최대 공약수를 구해야 해서 리스트를 집합을 만들어준다
    set_m = set(m_)
    common_divisors = set_n & set_m # 두 리스트의 교집합을 구한다
    max_common_divisor = max(common_divisors) #교집합중 최대값을 찾는다
    answer.append(max_common_divisor)  #나온 최대 공약수를 답 리스트에 넣어준다

    common_multiple = n*m//max_common_divisor #최소 공배수는 n과m을 곱하여
    answer.append(common_multiple) # 최대 공약수 로 나눠주면 된다 답에 넣어준다

    return answer


n = 2
m = 5
print(solution(n, m))
