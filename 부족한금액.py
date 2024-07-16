# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
# 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번
# 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다.
# 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서
# 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.
# price	money	 count  	result
#   3	 20     	4	     10


def solution(price, money, count):
    # 총금액을 구하기 위해서 가격 곱하기 횟수를 해준다 그리고 모두 더해준다
    totalcost = sum(price*i for i in range(1, count+1))
    # 내가 가진돈에서 총 금액을 빼준다
    result = money - totalcost
    # 값이 0보다 작다면
    if result < 0:
        # 결과를 리턴 한다 그런데 답에서는 얼만큼 부족한지 즉 
        # 양수가 필요하기 때문에 - 를 resul 에 넣어 준다
        return -result
    # 부족하지 않다면 0 을 리턴한다
    else:
        return 0


price = 3
money = 20
count = 4
print(solution(price, money, count))
