'''
numbers	target	return
[1, 1, 1, 1, 1]	3	5
'''

def solution(numbers, target):

    return dfs(numbers,target,0,0)

def dfs(numbers,target,index,num) :
    if index == len(numbers) :
        return 1 if num == target else 0
    return dfs(numbers,target,index+1,num+numbers[index]) + dfs(numbers,target,index+1,num-numbers[index])

print(solution([1, 1, 1, 1, 1],3))