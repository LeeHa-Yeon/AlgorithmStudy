# 문제18 : 평균 점수
# 공백으로 구분하여 세 과목의 점수가 주어지면 전체 평균 점수를 구하는 프로그램 작성하라
# 단, 소숫점 자리는 모두 버립니다.

subject = list(map(int, input().split()))

print(sum(subject)//len(subject))