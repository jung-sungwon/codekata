# 문자열 s의 길이가 4 혹은 6이고, 숫자로만
# 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고
# "1234"라면 True를 리턴하면 됩니다.

def solution(s):
    # 길이를 확인하는 len 함수 사용 4또는 6의 길이가 맞는지 확인
    # 문자열이 숫자로만 구성되어있는지 확인 하기 위해 s.isdigit() 사용
    # 모든게 맞다면 True 아니라면 False 
    if (len(s)==4 or len(s)==6) and s.isdigit():
        return True
    else:
        return False


s = 'asdd'
print(solution(s))
