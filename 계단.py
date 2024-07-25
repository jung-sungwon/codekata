

# n의 정상 만큼 오르는 경우의 수
# 계단 은 1칸 또는 2칸 씩 오를수있다
# e.g.
# n이 3 이면
# 1 1 1
# 1 2
# 2 1  총 3가지의 방법으로 오를수있다 함수를 만들어라

way = [1, 2, 3]  # 1 2 3 의 값


def how_many_way(n):  # 계단 오르기 방법 찾기 함수
    if n < 4:        # n이 4보다 작으면 n를 리턴 그 이유는 값과 n값이 같기 때문
        return n
    else:
        result = how_many_way(n-1) + ((how_many_way(n-1) - how_many_way(n-2))
                                      ) + ((how_many_way(n-3) - how_many_way(n-4)))
        if result not in way:  # 모든 연산결과를 넣지않고 필요한 값만 넣기 위함
            way.append(result)
        return result


# 4부터는 재귀함수를 통해 답을 찾게되는데 n 값은 n-1의 값 + n-2 에서 n-1의 증가량 더하기
# n-4 에서 n-3의 증가량 을 더하면 구할수 있었다 그 공식을 위에 적은것임
# e.g. 5의 값을 구하고싶다면 4의결과 5 더하기 3에서4까지 증가량(2)과 1에서 2증가량(1)을 더하여
# 8이 된다
#
for i in range(10):
    print(f"how_many_way({i}) = {how_many_way(i)}")
print(way)
