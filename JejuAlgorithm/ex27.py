# 문제27 : 딕셔너리 만들기
# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고, 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.
# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요

studentName = list(input().split(' '))
mathScore = list(map(int,input().split(' ')))

print(dict(zip(studentName,mathScore)))