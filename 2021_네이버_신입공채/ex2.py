'''

sentence , keyword, idxList   result
i love coding  mask  [0,0,3,2,3,4]    mai lsovke cmodinag
i love coding  mode  [0,10]            mi loove coding
abcde fghi      xyz  [10,0,1]         abcde fghixy
encrypt this sentence    something  [0,1,3,2,1,2,0,3,0,2,4,1,3]     seoncrmypett thihisng ssenteonmcee
'''



def solution(sentence,keyword,sept) :

    keyword_a = keyword
    for i in range(len(sept)) :
        if i+1 > len(keyword) :
            idx = (i+1) % len(keyword)
            keyword_a+=keyword[idx-1]
    keyword = keyword_a


    sentence_a = list(sentence)
    before = 0
    for j in range(len(sept)) :
        if keyword[j] in sentence_a[before:before+sept[j]]:

            sameIdx = sentence_a[before:before+sept[j]].index(keyword[j])
            sentence_a.insert(before+sameIdx,keyword[j])
            before += sept[j] + 1

        elif len(sentence_a) >= before+sept[j] :
            sentence_a.insert(before+sept[j],keyword[j])
            before += sept[j] + 1



    return "".join(sentence_a)




print(solution("i love coding","mask", [0,0,3,2,3,4]))
print(solution("i love coding" ,"mode", [0,10]))
print(solution("abcde fghi", "xyz" ,[10,0,1] ))
print(solution("encrypt this sentence","something" ,[0,1,3,2,1,2,0,3,0,2,4,1,3]))
