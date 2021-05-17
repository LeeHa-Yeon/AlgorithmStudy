'''
s	result
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0
'''

'18m'

def solution(s):
    cnt = 0

    # 회전하는 sList만들기
    sList =list(s)
    for _ in range(len(s)) :
        sList.append(sList.pop(0))
        standard = "".join(sList)

        # 그 리스트가 올바른 괄호인지 판단하기
        while standard.find('()') != -1 or standard.find('[]') !=-1 or standard.find('{}') != -1 :
            if standard.find('()') != -1 :
                standard = standard.replace('()','')
            if standard.find('{}') != -1 :
                standard = standard.replace('{}','')
            if standard.find('[]') != -1 :
                standard = standard.replace('[]','')
        if standard == "" :
            cnt+=1
    return cnt

print(solution("}}}"))