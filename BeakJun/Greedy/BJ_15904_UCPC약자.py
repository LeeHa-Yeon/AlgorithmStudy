# Union of Computer Programming Contest club contest
# University Computer Programming

sentence = input()
checking = ['U','C','P','C']
totalStr = ''
check = True


# 대문자로 함축시키는 작업
for i in sentence :
    if i.isupper() :
        totalStr+=i

# UCPC 순서대로 있는지 확인

for j in range(len(checking)) :
    if checking[j] in totalStr :
        idx = totalStr.find(checking[j])
        totalStr = totalStr[idx+1:]
        check = True
    else :
        check = False
        break


if check == True:
    print("I love UCPC")
else :
    print("I hate UCPC")