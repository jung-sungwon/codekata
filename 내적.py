# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다.
# a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

# 이때, a와 b의 내적은
# a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다.
# (n은 a, b의 길이)

# a	                b	      result
# [1,2,3,4] 	[-3,-1,0,2]     3
# [-1,0,1]	    [1,0,-1]	    -2


def solution(a, b):
    a_list = []
    # 내적을 구하기 위해서 zip으로 a,b를 묶어서꺼낸다
    for num1, num2 in zip(a, b):
        # a 와 b 에서 꺼넨 두 수를 곱하여 리스트에 넣어준다
        a_list.append(num1*num2)
    #리스트의 수를 합쳐준다 그러면 내적이 나온다 
    result = sum(a_list)
    answer = result
    return answer


a = [1, 2, 3]
b = [4, 5, 6]
print(solution(a, b))
