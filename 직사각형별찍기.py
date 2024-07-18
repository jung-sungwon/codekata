# 문제 설명
# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

# 입력

# 5 3
# 출력

# *****
# *****
# *****

# 여기까지는 지어진 문제 그래도 설명을 해보면
# map 은 어떤 한 기능을 반복가능한 요소에 모두 적용해준다
# 그래서 사용자에게 입력 받은 수의 양쪽 공백을 strip 으로 없애고
# 가운데 공백으로 나누면 문자열 2가지 요소가 있는 리스트가 되는데
# 그걸 인트로 숫자로 변경하여 a b 에 지정해 준다
a, b = map(int, input().strip().split(' '))
# 입력받은 a 만큼 *을 곱해주고 줄바꿈을 해주기 위해 \n 을 더해준다 그리고 b 만큼 곱해주면 끝
star = (a * '*' + '\n')*b
print(star)
