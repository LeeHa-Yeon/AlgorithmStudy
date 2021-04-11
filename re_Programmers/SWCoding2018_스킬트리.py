'''
skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2

못 풀었고 - 시간 너무 많이 걸려서 - 다른 사람 코드 보고 이해함
'''

def solution(skill, skill_trees):
    cnt = 0

    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0) :
                    break
        else:
            cnt += 1

    return cnt

# print(solution("CBDK" ,["ABC","CDB", "CBKD"]))
# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
# print(solution("CBDK" ,["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]))
# "CBD" ["CAD"] 0
# "CBD", ["AEF", "ZJW"] 2
# "REA" ,["REA", "POA"] 1
# "CBDK" ,["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"] 4
# "BDC", ["AAAABACA"] 0
# "CBD", ["C", "D", "CB", "BDA"] 2

print(solution("CBD", ["C", "D", "CB", "BDA"]))