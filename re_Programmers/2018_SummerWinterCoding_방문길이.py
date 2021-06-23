'''
dirs	answer
"ULURRDLLU"	7
"LULLLLLLU"	7
'''

def solution(dirs):
    firstLocation= (0,0,0,0)
    dx,dy =0,0
    s = set()

    for i in dirs :
        x,y = dx,dy
        beforeLocation = firstLocation
        if i == "U" and firstLocation[3]+1<=5:
            dy = firstLocation[3]+1
        elif i == "D" and firstLocation[3]-1>=-5:
            dy = firstLocation[3]-1
        elif i == "L" and firstLocation[2]-1>=-5:
            dx = firstLocation[2]-1
        elif i == "R" and firstLocation[2]+1<=5:
            dx = firstLocation[2]+1
        firstLocation = (x,y,dx,dy)
        if firstLocation[0]==firstLocation[2] and firstLocation[1]==firstLocation[3] :
            continue
        if beforeLocation[0]==firstLocation[2] and beforeLocation[1]==firstLocation[3] and beforeLocation[2]==firstLocation[0] and beforeLocation[3]==firstLocation[1] :
            continue
        s.add(firstLocation)
        print(s)

    return len(s)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LRLRL"))