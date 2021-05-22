'''
numbers	return
"17"	3
"011"	2
'''


from itertools import permutations

def isPrime(num) :
    if num == 1 or num == 0 :
        return 0
    else :
        for i in range(2,num) :
            if num%i == 0 :
                return 0
    return 1

def solution(numberStr) :
    perList= []
    cnt = 0

    for i in range(1,len(numberStr)+1) :
        perList.extend(list(map("".join, permutations(list(numberStr), i))))
    setList = set(map(int,perList))

    for i in setList :
        cnt+=isPrime(i)

    return cnt

print(solution("17"))




# a= list(map("".join,permutations(list(numberStr),2)))