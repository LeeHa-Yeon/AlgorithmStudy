'''
record	result
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

'''


def solution(record):
    answer = []
    userList = dict()

    for i in record :
        userid = i.split(" ")[1]
        if "Enter" in i or "Change" in i :
            userName = i.split(" ")[2]
            userList[userid]= userName

    for i in record :
        item = i.split(" ")
        if item[0] == "Change" :
            continue
        elif item[0] == "Enter" :
            answer.append(userList[item[1]]+"님이 들어왔습니다.")
        elif item[0] == "Leave" :
            answer.append(userList[item[1]]+"님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
