'''
absolutes	signs	result
[4,7,12]	[true,false,true]	9
[1,2,3]	[false,false,true]	0
'''

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)) :
        if signs[i] :
            answer+=absolutes[i]
        else :
            answer -= absolutes[i]
    return answer
