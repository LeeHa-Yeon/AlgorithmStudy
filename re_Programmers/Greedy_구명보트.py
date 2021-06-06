'''
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3


'''

def solution(people, limit):
    cnt = len(people)
    people.sort(reverse=True) # 50 50 70 80
    front,last = 0, len(people)-1
    while front<last :
        #print(people[front],people[last])
        if people[front] + people[last] <= limit :
            last-=1
            cnt-=1
        front+=1

    return cnt



print(solution([70, 50, 80, 50],100))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,40,50,45,45,100],100))
# print(solution([20, 50, 50, 100,150,110,200],250))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,200],200))
# print(solution([20, 50, 50, 80,200],200))