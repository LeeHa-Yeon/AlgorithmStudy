'''
people	            limit	return
[70, 50, 80, 50]	100	    3
[70, 80, 50]	    100 	3
'''


def solution(people, limit):
    cnt = 0
    people.sort() # 50 50 70 80
    front,last = 0, len(people)-1
    while front <= last :
        cnt+=1
        if people[front] + people[last] <= limit :
            front+=1
        last-=1

    return cnt

print(solution([70, 50, 80, 50],100)) #2

'''

'''