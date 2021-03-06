'''
m	musicinfos	answer
"ABCDEFG"	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"HELLO"
"CC#BCC#BCC#BCC#B"	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	"FOO"
"ABC"	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"WORLD"
'''

from itertools import chain,repeat
def solution(m, musicinfos):
    mLen = len(m.replace("#",""))
    answer=dict()

    for musicinfo in musicinfos :
        musicSplit = musicinfo.split(",")
        musicTime = int(musicSplit[1][3:])-int(musicSplit[0][3:])
        if mLen > musicTime :
            continue
        if musicTime < len(musicSplit[3]) :
            musicSplit[3] = musicSplit[3][:musicTime]
        repeatSheet = "".join(list(chain.from_iterable(repeat(musicSplit[3],len(m)//len(musicSplit[3])+1))))
        print(repeatSheet)
        if repeatSheet.find(m) != -1 :
            answer[musicTime]=musicSplit[2]

    if len(answer) > 1 :
        return answer[list(sorted(answer.keys(),reverse=True))[0]]
    if len(answer) == 1 :
        return answer.popitem()[1]

    return "(None)"


print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCD"]))

'''
1. 먼저 m의 길이가 음악시간에 포함되는지 확인
2. 포함되면 체인을 이용하여 반복한 문자열을 만들기
3. 곡 이름 반환
'''