# 문제 69번 : 골드 바흐의 추측
# 골드바흐의 추측은 오래전부터 알려진 정수론의 미해결 문제로,
# 2보다 큰 모든 짝수는 두 개의 소수의 합으로 표시할 수 있다는 것이다.
# 이때 하나의 소수를 두 번 사용하는 것은 허용한다.
#
# 위 설명에서 2보다 큰 모든 짝수를 두 소수의 합으로 나타낸 것을 골드바흐 파티션이라고 합니다
#
# 예 ) 100 == 47 +53
#        56 == 19+37
#
# 2보다 큰 짝수 n이 주어졌을 때, 골드바흐 파티션을 출력하는 코드를 작성하세요.
# - 해당 문제의 출력 형식은 자유롭습니다. 가능하시다면 골드바흐 파티션 모두를 출력하거나, 그 차가 작은 것을 출력하거나 그 차가 큰 것 모두 출력해보세요.
from itertools import combinations_with_replacement

def prime(n) :
    sosuSet = set(range(2,n+1))
    for i in range(2,n+1) :
        if i in sosuSet :
            sosuSet-=set(range(i*2,n+1,i))
    return sosuSet

def solution(n,primeSet) :
    answer = []
    for i in combinations_with_replacement(primeSet,2) :

        if i[0]+i[1] == n :
            answer.append([i[0],i[1]])
    return answer

n = int(input())
print(solution(n,prime(n)))


'''
< 순열,조합에 대한 링크 >
https://velog.io/@hayeon/순열조합중복순열중복조합
'''