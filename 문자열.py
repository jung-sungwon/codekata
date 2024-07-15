# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로
# 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

#    s	         return
# "Zbcdefg"	    "gfedcbZ"

def solution(s):
    # 문자를 오름차순으로 정렬하기 위해 sorted 를 사용 그것을 뒤집어(reverse) 
    # 내림차순으로 변경, 변경된 수는 이터레이터 이기때문에 조인으로 다시 묶어줌
    answer = ''.join(sorted(s, reverse=True))
    return answer


s = "acbdeasdasdfg"

print(solution(s))
