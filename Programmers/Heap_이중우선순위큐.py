'''
operations	return
[I 16,D 1]	[0,0]
[I 7,I 5,I -5,D -1]	[7,5]
'''

import heapq

def solution(operations):
    answer = []
    heapq.heapify(answer)

    while operations :
        word = operations.pop(0)

        if word[0] == "I" :
            num = word[2:]
            heapq.heappush(answer,int(num))
        elif word[0] == "D" and answer :
            if word[2] == '1' :
                maxValue = heapq.nlargest(1, answer)
                answer.remove(int(maxValue[0]))
            else :
                minValue = heapq.nsmallest(1, answer)
                answer.remove(int(minValue[0]))


    if answer == [] :
        answer = [0,0]
    else :
        maxValue = heapq.nlargest(1, answer)
        minValue = heapq.nsmallest(1, answer)
        answer.clear()
        answer.append(maxValue[0])
        answer.append(minValue[0])

    return answer

# print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))