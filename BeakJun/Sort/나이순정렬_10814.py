n = int(input())
singUp_list = []

for _ in range(n) :
    memberAge,memberName = input().split(" ")
    memberAge = int(memberAge)
    singUp_list.append((memberAge,memberName))

singUp_list.sort(key=lambda x:x[0])

print(singUp_list)

for a,b in singUp_list :
    print(a,b)