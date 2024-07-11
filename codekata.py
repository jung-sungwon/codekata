# 코드카타 문제
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
def solution(arr, divisor):
    answer = []
    # answer 라는 빈 리스트를 만들어 줬다
    for i in arr:
    # arr 을 한번씩 돌면서 나눠줘야해서 for 문으로 한바퀴 돌아보자
        if i % divisor == 0:
    # if 문을 써서 arr 안에 있는 element 를 dicisor 로 나누어
    # 나머지가 0 으로 떨어지는지 확인
            answer.append(i)
    # 나누어 0으로 떨어지면 answer list 에 append 해준다
    if not answer:
    # answer 에 아무것도 들어가지 않으면
        return [-1]
    # -1 을 반환해라
    return sorted(answer)
    # aswer를 반환할때는 오름 차순으로 반환해라


# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# divisor = 2

# result = solution(arr, divisor)
# print(result)
