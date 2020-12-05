# 문제28 : 2-gram
# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다. 예를 들어 'Python'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다.

user_input = input()

for i in range(len(user_input)-1) :
    print(user_input[i]+user_input[i+1])