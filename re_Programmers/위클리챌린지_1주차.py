'''
price	money	count	result
3	20	4	10
'''

def solution(price, money, count):
    answer = price
    for i in range(2,count+1) :
        answer+=(price*i)
    result = answer-money
    if result <= 0 :
        return 0
    return result

print(solution(3,20,4))