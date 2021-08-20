n = int(input())
group_list = list()
cnt = 0

for i in range(n) :
    group_list.append(input())

while group_list :
    word = group_list.pop(0)

    for idx in range(len(word)) :
        if idx != len(word)-1 :
            if word[idx] == word[idx+1] :
                continue
            elif word[idx] in word[idx+1:] :
                break
        else :
            cnt+=1
print(cnt)