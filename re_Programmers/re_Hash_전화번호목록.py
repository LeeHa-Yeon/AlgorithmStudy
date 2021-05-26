'''
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''

def solution(phone_book):
    phone_book.sort()
    if len(phone_book) == 1 :
        return True
    for standard,next in zip(phone_book,phone_book[1:]):
        if standard == next[:len(standard)] :
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))