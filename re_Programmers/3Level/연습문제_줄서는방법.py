'''
n	k	result
3	5	[3,1,2]

<처음 풀이 방식>
from itertools import permutations
def solution(n, k):
    firstLine = list(range(1, n + 1))
    lines = list(permutations(firstLine, len(firstLine)))[k - 1:k]

    return lines.pop()

=> 정확도 12,13 시간초과 , 효율성 0점
=> 원인 : n의 범위가 20이하의 자연수이기 때문에 permutaions 같은 n!의 반복횟수를 가지는 방법을 쓰면 시간초과가 발생한다.
=> 해결 : factorial

< factorial 풀이방식 >
1. n명을 줄 세우는 방법의 수는 n!
2. 첫번째 자리가 정해진 후 나머지의 줄 서는 방식의 수는 n-1!가지
   ( 1번이 첫번째 자리일 경우 2가지 , 2번이 첫번째 자리일 경우도 2가지, 3번이 첫번째 자리일 경우도 2가지 )
    =>  순열의 순원리도 factorial과 같음
    =>  첫번째 자리 정해져 있을 경우 : nP1 * (n-1)!
    =>  두번째 자리까지 정해져 있을 경우 : nP2 * (n-2)!
3. k-1 // factorial 로 나눈 이유 ( line에서 해당 인덱스를 찾아 pop 하기 위함 )
    => k-1은 직관적으로는 k번째이지만 인덱스로 따지면 k-1번째이기 때문에
    => 그냥 구체적으로 설명하자면
       1) line = [1,2,3]
         K-1번째    : 앞자리
         0번째 ~ : 1
         2번째 ~ : 2
         4번째 ~ : 3
         => (k-1) // (n-1)! = line의 인덱스 ( 찾고자 하는 사람번호 )
       2) line2 = [1,2,3,4]
         i+(n-1)!=k번째  : 앞자리
         1번째 ~ : 1
         7번째 ~ : 2
         13번째 ~ : 3
         19번째 ~ : 4
         => (k-1) // (n-1)!  = "line의 인덱스"
            (k-1) = 0,1,2,3,4,5까지는 "line의 인덱스"가 1
            (k-1) = 6,7,8,9,10,11까지는 "line의 인덱스"가 2
            (k-1) = 12,13,14,15,16,17까지는 "line의 인덱스"가 3
            (k-1) = 18,19,20,21,22,23까지는 "line의 인덱스"가 4
4. k %= factorial 한 이유
   => k를 차례대로 줄이는 과정

=> 구현은 permutations을 쓰면 되지만 시간초과로 순열의 순원리인 factorial을 이용하여 원하는 부분만 출력해야함
'''

from math import factorial as f

def solution(n, k):
    result = []
    # 1~n까지의 배열 생성
    line = list(range(1, n + 1))

    while line:
        # 맨 앞자리수가 같은 수의 개수는 (n-1)!
        factorial = f(len(line) - 1)
        # 차례대로 존재하는 line 앞자리수의 인덱스를 구하기
        result.append(line.pop((k - 1) // factorial))
        k %= factorial

    return result

print(solution(4,5))
