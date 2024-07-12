# 단어 s의 가운데 글자를 반환하는 함수,
# solution을 만들어 보세요. 단어의 길이가
# 짝수라면 가운데 두글자를 반환하면 됩니다.

#   s	       return
# "abcde"   	"c"
# "qwer"    	"we"

def solution(s):
    # s의 길이를 구하여 2로 나눈 정수값을 만든다(2로 나눈 정수값은 곧 홀수의 중앙이 된다)
    mid_char = len(s)//2
    #짝수면 문자를 슬라이싱 해서 2개를 보여주는 데 정수값에 -1:+1 한다
    # 이유는 [:] 슬라이싱을 사용하면 [start:end]에서 end 는 포한되지않는다
    # e.g. mid_char가 3일때 (짝수기준) 3-1 :3+1 이 다 2:4 다 그럼 자리수 2,3 번이 출력된다
    if len(s) % 2 == 0:
        return s[mid_char-1:mid_char+1]
    else:
        # mid_char 값은 곧 홀수의 정 중앙이기에 바로 반환한다
        return s[mid_char]


s = "asdasdw"
print(solution(s))
