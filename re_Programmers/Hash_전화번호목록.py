# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false



def solution(phone_book) :
    phone_book.sort()
    index = 0

    while index < len(phone_book)-1 :
        standard = phone_book[index]
        comparison = phone_book[index + 1]
        n = len(standard)
        if standard[0:n] == comparison[0:n] :
            return False
        index+=1

    return True

print(solution(["12","123","1235","567","88"]))




'''
def solution(phone_book):
    phone_book.sort()
    phone_book = list(map(str,phone_book))

    while len(phone_book) > 1 :
        standard = phone_book.pop(0)
        for i in phone_book :
            if i.find(standard) != -1 :
                return False

    return True
'''