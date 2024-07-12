# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부
# *으로 가린 문자열을 리턴하는 함수,solution을 완성해주세요.
# e.g.  phone_number	    return
#       "01033334444"	"*******4444"
#       "027778888"	    "*****8888"


#  문자열을 뒤에 네자리 기준으로 분리하고
#  나머지를 * 처리 한다
def solution(phone_number):
    # 문자열을 분리 하기 위해 슬라이싱 사용
    last_num = phone_number[-4:]
    first_num = phone_number[:-4]
    # 꺼낸 마지막 4자리를 제외한 수를 기리를 구하여 길이만큼 *에 곱해준다
    cg_num = '*'* len(first_num)
    # *로 번한 앞의 수와 그대로인 뒤에수를 더해준다
    answer = cg_num + last_num
    return answer

# phone_number = "01011111111"

# print(solution(phone_number))

# 딱 보아도 뭔가 코드가 지져분 하다 앞으로 클린코드 연습도 같이 해야겠다