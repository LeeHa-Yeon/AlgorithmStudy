# 문제 : count 사용하기
# 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 했다
# 입력 - 첫 줄에 학생들이 뽑은 후보들이 입력됩니다.
# 원영 원영 은비 은비 은비 채연 채연
# 출력 - '은비가 총 4표로 반장이 되었습니다.'와 같습니다.


candidate_list = input().split()
candidate_set = set(candidate_list)
maxNum = 0
for i in candidate_set :
    if maxNum < candidate_list.count(i) :
        maxNum = candidate_list.count(i)
        electCandidate = i

print('{}가 총 {}표로 반장이 되었습니다.'.format(electCandidate,candidate_list.count(electCandidate)))

