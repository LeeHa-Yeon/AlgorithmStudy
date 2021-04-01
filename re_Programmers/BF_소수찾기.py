# numbers	return
# "17"	3
# "011"	2


from itertools import permutations

def Sosu(num) :
    if num != 1 :
        for i in range(2,num) :
            if num%i == 0 :
                return False
    else :
        return False
    return True

def solution(numberStr) :
    numberList = list(map(int,numberStr))
    l = []
    l2 = set()
    cnt = 0

    # 모든 경우의 숫자 만들기
    for i in range(1,len(numberStr)+1) :
        l += list(permutations(numberList,i))

    # 숫자 합쳐서 중복제거
    for i in l :
        strA = ""
        for j in i :
            strA+=str(j)
        l2.add(int(strA))


    # 소수인지 확인하기
    for i in l2 :
        if Sosu(i) and i > 1 :
            cnt+=1
    return cnt

print(solution("011"))




