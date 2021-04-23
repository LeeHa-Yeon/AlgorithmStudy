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
        while m <= len(s) :
            standard = s[j:m]
            j += n
            m += n
            comparison = s[j:m]
            if standard == comparison :
                cnt += 1
            else :
                if cnt == 1 :
                    result += comparison
                else :
                    result += str(cnt) + comparison
                cnt = 1
        answer.append(len(result))
        n+=1

    return min(answer)

print(solution("aabbaccc"))

