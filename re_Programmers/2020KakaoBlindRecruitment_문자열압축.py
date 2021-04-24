'''
s	result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
'''

def solution(s):
    answer = []
    n = 1
    while n <= len(s) :  # n : 짜르는 문자열의 길
        j = 0
        m = n
        cnt = 1
        result = s[j:m]
        print("n",n)
        while m <= len(s) :
            standard = s[j:m]
            j += n
            m += n
            comparison = s[j:m]
            if standard == comparison :
                print("같음", standard, comparison)
                cnt += 1
            else :
                print("다름",standard,comparison)
                if cnt == 1 :
                    result += comparison
                else :
                    result += str(cnt) + comparison
                cnt = 1
        answer.append(len(result))
        print('----------')
        n+=1

    return min(answer)

print(solution("aabbaccc"))



''' 한개 비교 햇을 때
result = s[0]  # 첫번째 값을 결과에 넣는다
count  = 0   #

for st in s:
    if st == result[-1]:  #
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print result

'''


''' 여러개 비교 했을 때 
def solution(s):
    answer = []
    n = 1
    while n <= len(s) :  # n : 짜르는 문자열의 길
        j = 0
        m = n
        cnt = 1
        result = s[j:m]
        print("n",n)
        while m <= len(s) :
            standard = s[j:m]
            j += n
            m += n
            comparison = s[j:m]
            if standard == comparison :
                print("같음", standard, comparison)
                cnt += 1
            else :
                print("다름",standard,comparison)
                if cnt == 1 :
                    result += comparison
                else :
                    result += str(cnt) + comparison
                cnt = 1
        answer.append(len(result))
        print('----------')
        n+=1

    return min(answer)

print(solution("aabbaccc"))

'''
