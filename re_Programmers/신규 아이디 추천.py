'''
no	new_id	result
예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	"z--"
예3	"=.="	"aaa"
예4	"123_.def"	"123_.def"
예5	"abcdefghijklmn.p"	"abcdefghijklmn"

'''

def first_rule(new_id) :
    return new_id.lower()

def second_rule(new_id) :

    removeStr = ""

    for i in new_id :
        # 이 메서드는 변수가 문자열이고, 모든 문자와 숫자인 경우엔 True, 아니면 False
        if i.isalnum() == False and i != '-' and i != '_' and i != '.' :
            continue
        else :
            removeStr+=i
    return removeStr

def third_rule(new_id) :

    while new_id.find("..") != -1 :
        new_id = new_id.replace("..",".")
    return new_id


def fourth_rule(new_id) :
    new_id = list(new_id)

    if new_id[0] == '.' :
        new_id.pop(0)

    if new_id != [] and new_id[len(new_id)-1] == '.' :
        new_id.pop(len(new_id)-1)

    return ''.join(new_id)

def fifth_rule(new_id) :

    if new_id == '' :
        new_id = 'a'

    return new_id


def sixth_rule(new_id) :
    if len(new_id) >= 16 :
        new_id = new_id[:15]
    return new_id

def final_rule(new_id) :
    last_str = new_id[-1]
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id+=last_str
    return new_id


def solution(new_id):
    new_id = first_rule(new_id)
    new_id = second_rule(new_id)
    new_id = third_rule(new_id)
    new_id = fourth_rule(new_id)
    new_id = fifth_rule(new_id)
    new_id = sixth_rule(new_id)
    new_id = fourth_rule(new_id)
    new_id = final_rule(new_id)
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))