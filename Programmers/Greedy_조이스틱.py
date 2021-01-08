def solution(name):

    answer  = 0

    l = ["A" for _ in range(len(name))]

    for k in range(len(name)) :
        i = name[k]
        j = l[k]
        if ord(i) == 65 :
            answer-=1
            continue
        if ord(i) <= 77 :
            answer+= ord(i)-ord(j)
            #print('test2',answer)
        else :
            answer+= 26-(ord(i)-ord(j))
            #print('test3',answer)
    return answer+len(name)-1

print(solution("JEROEN"))