# 문제 : 콤마 찍기
# 숫자를 입력 받고 천단위로 콤마(,)를 찍어주세요.
# 예를 들어 123456789를 123,456,789를 출력해야합니다.

num = '1234567897'

def insertComma(taget) :
    if len(taget) <= 3 :
        return taget
    else :
        return insertComma(taget[:len(taget)-3]) + ',' + insertComma(taget[len(taget)-3:])

print(insertComma(num))


'''

- insert
    중복된 값 삽입 불가
    최소 2개의 값 필요
    int값만 가능

- append
    리스트 맨 뒤에 데이터 추가
    중간에 원하는 인덱스로 추가시 (객체)[(인덱스):(인덱스)]
    
'''