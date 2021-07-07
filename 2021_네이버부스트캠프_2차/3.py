def solution(params):
    resiA = []
    resiB = []
    stackArr = []
    answer = []
    for i in params :
        if i=="PRINT" :
            if len(stackArr) == 0 :
                answer.append("EMPTY")
            else :
                answer.append(stackArr.pop())
        elif "PUSH" in i :
            if len(stackArr)==8 :
                answer.append("OVERFLOW")
            if i[4]=="0" or i[4]=="1" or i[4]=="2" or i[4]=="3" :
                stackArr.append(i[4])
            else :
                answer.append("UNKNOWN")
        elif "POP" in i :
            if len(stackArr) == 0 :
                answer.append("EMPTY")
            if i[3] == "A" and len(stackArr) > 0 :
                resiA.append(stackArr.pop())
            elif i[3]=="B" and len(stackArr) > 0  :
                resiB.append(stackArr.pop())
        elif "SWAP" in i :
            resiA,resiB = resiB,resiA
        elif "ADD" in i :
            if len(resiA)!=0 and len(resiB)!=0 :
                aPop=int(resiA.pop())
                bPop=int(resiB.pop())
                if len(stackArr)==8 :
                    answer.append("OVERFLOW")
                else :
                    stackArr.append(str(aPop+bPop))
            else :
                answer.append("ERROR")
        elif "SUB" in i :
            if len(resiA)!=0 and len(resiB)!=0 :
                aPop=int(resiA.pop())
                bPop=int(resiB.pop())
                if len(stackArr)==8 :
                    answer.append("OVERFLOW")
                else :
                    stackArr.append(str(abs(aPop-bPop)))
            else :
                answer.append("ERROR")
        else :
            answer.append("UNKNOWN")

    return answer


'''
["PRINT","PUSH0","PRINT","POPA"] # ["EMPTY","0","EMPTY"]
["PUSH1","PUSH1","PUSH2","POPA","POPB","SWAP","ADD","PRINT","PRINT"] # ["3","1"]
["PUSH3","PUSH2","PUSH1","POPA","POPB","SWAP","SUB","POPA","POPB","ADD","PRINT"] # ["4"]
["ADD","PUSH3","PUSH1","PUSH0","PUSH2","PUSH1","PUSH3","PUSH2","PUSH0","PUSH3","PUSH4"]  # ["ERROR","OVERFLOW","UNKNOWN"]
'''