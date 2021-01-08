def solution(name):

    AlphaUpDownCnt = list()
    answer  = 0

    # Alphabet up/down
    for word in name :
        AlphaUpDownCnt.append(min(ord(word)-ord('A'),26-(ord(word)-ord('A'))))
    answer+=sum(AlphaUpDownCnt)

    # Alphabet left/right
    idx = 0
    AlphaUpLeftRight = AlphaUpDownCnt[:]

    while True :
        AlphaUpLeftRight[idx] = 0
        left,right = 1,1
        if sum(AlphaUpLeftRight) == 0 :
            return answer
        # print(AlphaUpLeftRight,AlphaUpLeftRight[idx+right])
        while AlphaUpLeftRight[idx-left] == 0 :
            left+=1
        while AlphaUpLeftRight[idx+right] == 0 :
            right+=1
        answer+=left if left<right else right
        idx+= -left if left<right else right
        # print(left,right,idx)

print(solution("BBBAAAB"))

'''
테스트 케이스

print(solution(BBBAAAB)) #8
print(solution(ABABAAAAABA)) #10
print(solution(CANAAAAANAN)) #48
print(solution(ABAAAAABAB)) #8
print(solution(ABABAAAAAB)) #8
print(solution(BABAAAAB)) #7
print(solution(AAA)) #0
print(solution(ABAAAAAAABA)) #6
print(solution(AAB)) #2
print(solution(AABAAAAAAABBB)) #11
print(solution(ZZZ)) #5
print(solution(BBBBAAAAAB)) #10
print(solution(BBBBAAAABA)) #12

'''