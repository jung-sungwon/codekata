# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열
# absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가
# 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록
# solution 함수를 완성해주세요.
# e.g. absolutes	signs	        result
# [4,7,12]	[true,false,true]   	9
# [1,2,3]	[false,false,true]	    0

# 우선 문제 풀기 전에 생각 하기...  뭐가 필요할까
# 순서를 생각해 보자
# absolutes 에서 하나 signs 에서 하나 뺴서 true 면
# sum으로 묶어서 더해주고 false 가 나오면 -를 주고 더해준다

# def solution(absolutes, signs):
#     a_list = []
#     for i in absolutes:
#         a_list.append(i)

#     answer = sum(a_list)
#     return answer


# absolutes = [4, 7, 12]
# signs = [True, False, True]
# result = solution(absolutes, signs)
# print(result)
# 여기까지 생각한대로 우선 꺼내서 합치기 까지 성공 이제 참 거지의 조건에 따라 - 넣어줘야함
# ---------------------------------------------

def solution(absolutes, signs):
    # 빈 리스트 만들어 주기
    a_list = []
    # zip 함수로 ansolutes 와 Signs 를 쌍으로 묶어서 튜플로 꺼내준다
    for num, sign in zip(absolutes, signs):
        # 숫자와 True 또는 False 가 함께 묶여있는데 if (True) 이면 걍 그대로 둔다
        if sign:
            num = num
            # Fase면 숫자에 - 룰 붙여준다
        else:
            num = -num
            # 리스트에 넣어준다
        a_list.append(num)
    answer = sum(a_list)
    return answer
# 여기서 기억하고 집고 가야할것 zip 함수는 묶어서 튜플로 꺼내준다 순서대로
# 또한 zip 함수는 리스트의 길이가 서로 달라도 사용가능 하다 가장 짧은 리스트에
# element 수만큼만 출력된다 나머지 는 무시한다 
# if 는 내가 말해주지 않아도 기본적으로 참 거짓을 판단 할 준비를 하고 있다

absolutes = [4, 12, 12]
signs = [True, False, True]
result = solution(absolutes, signs)
print(result)
