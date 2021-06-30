'''
msg	answer
KAKAO	[11, 1, 27, 15]
TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
ABABABABABABABAB	[1, 2, 27, 29, 28, 31, 30]
'''

def solution(msg):
    answer = []
    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    word = dict()
    for i in range(0,26) :
        word[chr(65+i)]=i+1

    # 2. 사전에 추가할 새로운 인덱스, 길이를 늘릴 인덱스 선언
    wordLastIdx = len(word)+1
    msgPlusIdx = 0

    while msg :
        msgPlusIdx += 1
        # 3. 딕셔너리 안에 존재하지 않는 문자열이 나올때까지 길이 늘리기 -> 사전에 등록
        if msg[:msgPlusIdx+1] not in word :
            word[msg[:msgPlusIdx+1]]=wordLastIdx
            wordLastIdx+=1
            # 4. 최대 길이보다 하나 작은 문자열을 w로 지정 -> 바로 w 색인번호 출력
            answer.append(word[msg[:msgPlusIdx]])
            # 5. w 부분 제거
            msg = msg[msgPlusIdx:]
            msgPlusIdx =0
        else :
            if msgPlusIdx - 1 == len(msg):
                # 마지막 문자열 부분의 색인번호를 출력
                answer.append(word[msg])
                break

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
