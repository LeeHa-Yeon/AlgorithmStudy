'''
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''


# 정렬을 하면 접두어가 같은 부분이 있을때 앞부분분(standard)이 뒷부분(comparison)보다 길이가 짧음
# 그래서 길이를 standard로 설정해두고 슬라이스를 통해서 확인가능

def solution(phone_book):
    phone_book.sort()
    idx = 0

    while idx < len(phone_book)-1 :
        standard = phone_book[idx]
        comparison = phone_book[idx+1]
        n = len(standard)
        if standard[0:n] == comparison[0:n] :
            return False
        idx += 1
    return True


print(solution(["12","123","1235","567","88"]))
