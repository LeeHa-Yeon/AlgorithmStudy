


from collections import Counter
def solution(param0) :
    sameFile = []
    answer= []
    for i in param0 :
        while i.find("/")!=-1 :
            findIdx= i.find("/")
            i=i[findIdx+1:]
        sameFile.append(i[0]+i[-2:])
    sameCntFile = Counter(sameFile)

    for fileName,cnt in sameCntFile.items() :
        if cnt>=2 :
            answer.append(fileName)
            answer.append(str(cnt))
    return answer

print(solution(["/a/a_v2.x","/b/a.x","/c/t.z","/d/a/t.x","/e/z/t_v1.z","/k/k/k/a_v9.x"]))
print(solution(["/t.z","/z/z_v2.z","/a.z","/d/b.z","/d/a/t.z"]))
print(solution(["/t.z","/b/b.z","/a.z","/e/k.z","/d/a/x_v2.z"]))