'''
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

def solution(number, k):
    collection = [number[0]]
    for num in number[1:] :
        while collection and collection[-1] < num and k > 0 :
            collection.pop()
            k-=1
        collection.append(num)

    if k != 0 :
        collection = collection[:-k]

    return ''.join(collection)


print(solution("1924", 2), "94")
# print(solution("1231234", 3), "3234")
# print(solution("4177252841", 4), "775841")
# print(solution("99991", 3), "99")
# print(solution("111119", 3), "119")
# print(solution("7777777", 2), "77777")
# print(solution("10000", 2), "100")
# print(solution("87654321", 3), "87654")
# print(solution("01010", 3), "11")
