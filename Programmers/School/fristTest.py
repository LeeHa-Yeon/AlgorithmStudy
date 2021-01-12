def solution(src):
    cnt = 1
    startWord = list()
    startWord.append(src[0])

    for i in range(len(src)-1) :
        if src[i] == src[i+1] :
            cnt+=1
        else :
            word = chr(cnt + 64)
            startWord.append(word)
            cnt=1
    word = chr(cnt+64)
    startWord.append(word)


    return ''.join(startWord)

print(solution("111100100011"))