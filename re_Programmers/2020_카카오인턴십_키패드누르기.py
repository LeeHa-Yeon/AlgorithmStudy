'''
numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

'''

def manhattan_distance(r1,r2,c1,c2) :
    return abs(r1-r2) + abs(c1-c2)

def solution(numbers, hand):
    result = []

    phoneKeyped = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),"*":(3,0),0:(3,1),"#":(3,2)}
    phonekeyped_reverse = dict()
    current_left = phoneKeyped["*"]
    current_right = phoneKeyped["#"]

    for k,v in phoneKeyped.items() :
        phonekeyped_reverse[v] = k

    for i in numbers :
        # print(current_left,current_right)
        if i == 1 or i == 4 or i == 7 :
            current_left = phoneKeyped[i]
            result.append('L')
        elif i == 3 or i == 6 or i == 9 :
            current_right = phoneKeyped[i]
            result.append('R')
        else :
            templeft =phonekeyped_reverse[current_left]
            tempright = phonekeyped_reverse[current_right]
            distanceleft = manhattan_distance(phoneKeyped[i][0],phoneKeyped[templeft][0],phoneKeyped[i][1],phoneKeyped[templeft][1])
            distanceright = manhattan_distance(phoneKeyped[i][0],phoneKeyped[tempright][0],phoneKeyped[i][1],phoneKeyped[tempright][1])
            if distanceleft == distanceright :
                if hand == 'right' :
                    current_right = phoneKeyped[i]
                    result.append('R')
                else :
                    current_left = phoneKeyped[i]
                    result.append('L')
            else :
                if distanceleft < distanceright :
                    current_left = phoneKeyped[i]
                    result.append('L')
                else :
                    current_right = phoneKeyped[i]
                    result.append('R')



    return "".join(result)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))