'''
A 111 B 000 C 001 D 010 E 011 H 100 L 101

1. 만약 입력값이 "LD","LN"으로 시작하지 않거나 "LD","LN" 다음에 공백이 없으면 해석하지 않고 "ERROR" 리턴 ok
2. 레지스터 문자 값이 A,B,C,D,E,H,L 7종류 중 하나가 아니거나, 레지스터 값 다음에 콤마 ","가 없어도 "ERROR" 리턴 ok
3. "LD" 명령에서 src와 dst 레지스터가 같으면 의미 없는 명령이기에 "NOOP" 리턴  ok
16진수 변환시 모두 대문자로  ok
'''

import re
def solution(param0):
    param0 = re.split(' ',param0)

    if len(param0) > 1 :
        p = re.split('',param0[1])
        if p[2] != ',' :
            return "ERROR"
        if p[1]!='A' and p[1]!='B' and p[1]!='C' and p[1]!='D' and p[1]!='E' and p[1]!='H' and p[1]!='L' :
            return "ERROR"
        if param0[0]=="LD" and (p[3]!='A' and p[3]!='B' and p[3]!='C' and p[3]!='D' and p[3]!='E' and p[3]!='H' and p[3]!='L') :
            return "ERROR"
        a = re.split(',',param0[1])

    if param0[0]=="LD" :
        a[0] = a[0].replace('A','111').replace('B','000').replace('C','001').replace('D','010').replace('E','011').replace('H','100').replace('L','101')
        a[1] = a[1].replace('A','111').replace('B','000').replace('C','001').replace('D','010').replace('E','011').replace('H','100').replace('L','101')
        if a[0]==a[1] :
            return "NOOP"
        answer = boost_bin2hex(a[0],a[1])


    elif param0[0]=="LN" :
        a[0] = a[0].replace('A','111').replace('B','000').replace('C','001').replace('D','010').replace('E','011').replace('H','100').replace('L','101')
        answer = boost_dec2hex(a[0],a[1])
    else :
        return "ERROR"

    return answer

def boost_bin2hex(r1,r2) :
    # 8비트 2진수 문자열 입력으로 16진수 문자열로 바꿔서 리턴
    before = "0b"+"01"+r1+r2
    b = int(before,2)
    result = "0x"+hex(b)[2:].upper()
    return result

def boost_dec2hex(r1,n) :
    # 256 미만 10진수 입력으로 16진수 문자열로 바꿔서 리턴
    before = "0b"+"00"+r1+"110"+bin(int(n))[2:]
    b = int(before,2)
    result = "0x"+hex(b)[2:].upper()
    return result


'''
LD C,A "0x4F"
LN A,202 "0x3ECA"
LNA,B - error
'''