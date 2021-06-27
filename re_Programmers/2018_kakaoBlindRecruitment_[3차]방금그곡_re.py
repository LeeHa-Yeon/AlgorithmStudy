from itertools import chain,repeat
def solution(m, musicinfos):

    m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a").replace("E#","e")
    mLen = len(m)
    answer=dict()

    for musicinfo in musicinfos :
        musicSplit = musicinfo.split(",")
        musicSplit[3] = musicSplit[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("E#","e")
        if (int(musicSplit[1][:2]) - int(musicSplit[0][:2])) > 0 :
            musicTime = ((int(musicSplit[1][:2]) - int(musicSplit[0][:2]))*60) - (int(musicSplit[0][3:]) - int(musicSplit[1][3:]))
        else :
            musicTime = int(musicSplit[1][3:]) - int(musicSplit[0][3:])
        if mLen > musicTime:
            continue
        if musicTime < len(musicSplit[3]) :
            musicSplit[3] = musicSplit[3][:musicTime]
        repeatSheet = "".join(list(chain.from_iterable(repeat(musicSplit[3], mLen // len(musicSplit[3]) + 4))))
        if repeatSheet.find(m) != -1 and musicTime not in answer.values():
            answer[musicSplit[2]]=musicTime

    if len(answer) > 1 :
        return sorted(answer.items(), key=lambda x:x[1], reverse=True)[0][0]
    if len(answer) == 1 :
        return answer.popitem()[0]

    return "(None)"

print(solution("ABCDEFG",["12:50,13:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))