'''
N	result
5	2
6	2
5000	5
k칸 점프 => 건전지 k만큼 닳음
순간이동 => 현재까지 온 거리 * 2
'''


def solution(n):
    q,r = divmod(n,2)
    answer = r
    while q!=0 :
        q,r= divmod(q,2)
        if r == 1 :
            answer+=1
    return answer



print(solution(5))
print(solution(6))
print(solution(5000))