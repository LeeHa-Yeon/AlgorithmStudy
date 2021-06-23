'''
dirs	answer
"ULURRDLLU"	7
"LULLLLLLU"	7
'''

def solution(dirs):
    firstLocation= (0,0)
    dx,dy =0,0
    s = set()
    s.add(firstLocation)

    for i in dirs :
        if i == "U" :
            dy = firstLocation[1]+1
        elif i == "D" :
            dy = firstLocation[1]-1
        elif i == "L" :
            dx = firstLocation[0]-1
        elif i == "R" :
            dx = firstLocation[0]+1
        print(i,dx,dy)
        firstLocation = (dx,dy)
        s.add(firstLocation)

    return len(s)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))