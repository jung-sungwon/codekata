# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한
# 배열을 리턴하는 함수, solution을 완성해주세요. 단,
# 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.


def solution(arr):
    # arr 리스트의 element 가 1개 이상일 경우 arr에서 최소값을 제거 한다
    if len(arr) > 1:
        arr.remove(min(arr))
# 만약 한개 보다 작다면 -1 을 리턴해라
    else:
        return [-1]
    return arr


# arr = [100000]
# print(solution(arr))

# print(len(arr))
