'''
n	result
4	5

2*n

가로는 항상 2개 세로는 항상 1개 차지
2,2
2,1,1
1,2,1
1,1,2
1,1,1,1


< 내가 문제 푸기 위해 생각한 방식 >
최대한 2를 써보기
그 다음 각각 순열 돌린후 중복 포함 안되니 set으로 두기
예외처리 => 만약 가로의 길이가 1인 경우에는 return 1
=> 시간 초과

from itertools import permutations
def solution(n):

    if n == 1 :
        return 1
    cnt = 0
    q, r = divmod(n, 2)

    for q1 in range(q, -1, -1):
        tmp = []
        if r!=0 :
            for _ in range(r) :
                tmp.append(1)
        for _ in range(q1) :
            tmp.append(2)
        r+=2
        cnt += len(set(permutations(tmp,len(tmp))))

    return cnt

print(solution(4))

< DP, 메모이제이션 사용 >
n=1일때 1
n=2일때 2
n=3일때 n1+n2 = 1+2 = 3
n=4일때 n2+n3 = 2+3 = 5
n=5일때 n3+n4 = 3+5 = 8
n=6일때 n4+n5 = 5+8 = 13
이 문제에서 주의사항에 있는 1000000007을 나눠줘야된다.
마지막에만 나눠주는게 아니라 매 순간 나눠주는 것이 포인트 -> 효율성 부분에서 몇개 통과가 안됨

'''
def solution(n):
    dp = [1,2]
    for _ in range(2,n) :
        dp.append((dp[-1]+dp[-2])%1000000007)

    return dp[n-1]

print(solution(5))
