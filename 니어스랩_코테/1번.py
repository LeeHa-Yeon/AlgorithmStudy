# AAABBCCBCAAC
user_input = input()

compressionArr = user_input[0]

for word in user_input:
    if word != compressionArr[-1]:
        compressionArr += word

firstCnt = len(user_input)-len(compressionArr)


standard = user_input[0]
cnt = 1
secondCnt = 0

for word in user_input[1:] :
    if standard == word :
        cnt+=1
    else :
        if cnt != 1 :
            secondCnt += 1
        cnt = 1
        standard = word

if user_input[-1] == user_input[-2] :
    secondCnt += 1

print(firstCnt,end=" ")
print(secondCnt)

