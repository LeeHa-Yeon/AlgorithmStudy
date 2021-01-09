'''
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841
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



print(solution('999',2))


''' 58.3 / 100.0 -> 2,3,4,9,10 실패 (1~12)
def solution(number, k):
    answer = ''
    numList = list(map(int,number))

    idx = 0

    while k != 0 :
        test = numList[idx:idx + 3]
        print(test,numList)
        if numList[idx] == numList[idx+1] :
            idx+=1
            continue
        elif numList[idx] != numList[idx+1] :
            numList.pop(numList.index(min(test)))
            k-=1

    return "".join([str(i) for i in numList])
'''