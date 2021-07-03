'''
dirs	answer
"ULURRDLLU"	7
"LULLLLLLU"	7
'''

def solution(dirs):
    locationVisit = []
    cnt = 0
    bx,by,x,y = 0,0,0,0

    for dir in dirs :
        bx,by = x,y
        if dir=="U" and y<5:
            y+=1
        elif dir=="D" and y>-5:
            y-=1
        elif dir=="L" and x>-5 :
            x-=1
        elif dir=="R" and x<5 :
            x+=1
        if (bx,by,x,y) not in locationVisit :
            if (bx==x and by==y) :
                continue
            locationVisit.append((bx,by,x,y))
            locationVisit.append((x,y,bx,by))
            cnt+=1

    return cnt



print(solution("ULURRDLLU")) #7
print(solution("LULLLLLLU")) #7
print(solution("UDU")) # 1
print(solution("LLLLRLRLRLL")) # 5
print(solution("UUUUDUDUDUUU")) # 5
print(solution("LURDLURDLURDLURDRULD")) # 7
print(solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU")) # 11