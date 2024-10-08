# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행,
# 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수,
# solution을 완성해주세요.
# 입출력 예
# arr1	               arr2	              return
# [[1,2],[2,3]]    	[[3,4],[5,6]]   	[[4,6],[7,9]]
# [[1],[2]]	         [[3],[4]]	          [[4],[6]]


def solution(arr1, arr2):
    result = [[a[i]+b[i] for i in range(len(a))] for a, b in zip(arr1, arr2)]
    # 이해하기 정말 어려웠다 끊어서 말해보겠다
    # 우선 두 리스트를 짝지어 더해주어야 하니까 zip(arr1, arr2)로 하나씩 꺼내서 묶어준다
    # (arr1 과 arr2이 묶이는게 아니라 arr1 끼리 arr2 끼리)
    # for a, b in zip 으로 하나씩 빼서 이름을 a b 로 묶어 주었다(반복해서 끝까지) 
    # for a, b in zip(arr1,arr2) 의 a는 [1,2,3] 이고 b는 [2,4,5]이다 (한번 순회 했을때)
    # 두번째는 a는 [2,2,4] b는 [3,2,1]
    # for i in range(len(a)) 는 a의 길이를 측정해서 [1,2,3] 을 만나 3 이라는
    # 길이를 측정했을것이고 그럼 [[a[i]+b[i] for i in range(3)]과 같다
    # range(3)은 0,1,2 와 같다 (본인을 포함 하지 않기 때문)
    # [a[i]+b[i] 그럼 여기에 0,1,2 가 순서대로 들어가게 된다
    # a[0]+b[0] 이런식으로 그럼 a의 0번째 는 아까 zip으로 묶어서 만들었던
    # 튜플의 0번째 곧 첫번째 [1,2,3]중ㅇ에 1과 b의 1번째[2,4,5]중 2 가 더해진다
    # 순서대로 더해져서 [[3, 6, 8], [5, 4, 5]] 라는 결과가 나온다
    return result


arr1 = [[1, 2, 3], [2, 2, 4]]
arr2 = [[2, 4, 5], [3, 2, 1]]

print(solution(arr1, arr2))
