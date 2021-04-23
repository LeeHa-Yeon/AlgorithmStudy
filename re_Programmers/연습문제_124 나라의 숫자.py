'''
n	result
1	1
2	2
3	4
4	11
'''
# permuArr.append(set(map(''.join,permutations(numbers,i))))

def Ternary(number) :
    answer = ''
    while number >= 1:
        nDivmod = divmod(number, 3) # (몫,나머지)
        remain = nDivmod[1]
        number = nDivmod[0]
        answer = str(remain) + answer
        if len(answer) > 1 :
            if answer[0:3] == '100':
                answer = '24'
            elif answer[0:2] == '10' :
                answer = '04'+answer[2:len(answer)]
            elif answer[0:2] == '20' :
                answer = '14'+answer[2:len(answer)]

    return answer


def solution(number):

    ThreeJinsu = int(Ternary(number))


    return str(ThreeJinsu)


print(solution(9))



''' 비효율적 
from itertools import product

def solution(n):
    a = []
    aList = ['1','2','4']
    for i in range(1,3) :
        b = list(map(''.join,product(aList,repeat=i)))
        for i in range(len(b)):
            a.append(int(b[i]))
    print(a)
    return str(a[n-1])
'''