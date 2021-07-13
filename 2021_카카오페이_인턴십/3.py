'''
line1   line2   result
"abbbcbbb" "bbb"   4
"abcabcabc" "abc"   4
"abacaba"   "acb"   0
'''

def solution(line1,line2) :
    cnt = 0
    blank = 0

    line2a = ("_"*blank).join(line2)
    while len(line2a) <= len(line1) :
        for i in range(0,len(line1)-len(line2a)+1):
            line1a = line1[i:i+len(line2a)]
            cnt1 = 0
            for j in range(len(line2a)) :
                if line2a[j] == '_' :
                    continue
                if line1a[j] != line2a[j] :
                    cnt1+=1
                    break
            if cnt1 == 0 :
                cnt+=1
        blank+=1
        line2a = ("_"*blank).join(line2)
    return cnt

print(solution("abbbcbbb","bbb"))
print(solution("abcabcabc","abc"))
print(solution("abacaba","acb"))
