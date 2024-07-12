# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열
# numbers가 매개변수로 주어집니다. numbers에서
# 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한
# 수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# numbers	            result
# [1,2,3,4,6,7,8,0]	       14       1~9까지중 5와9가 없기때문
# [5,8,4,0,6,7,9]	        6       1,2,3 이없기 때문

def solution(numbers):
    # 1~9 까지의 집합을 만들어줌
    num_set = set(range(1, 10))
    # numbers 의 집합도 만들어줌
    numbers_set = set(numbers)
    # 1~9 집합 에서 변수 집합을 뻬줌 그럼 없는 수가 나옴
    missing_num =  num_set - numbers_set
    # 없는수 더해주기
    answer = sum(missing_num)
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7]

print(solution(numbers))
