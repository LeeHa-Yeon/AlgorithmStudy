import sys
N = int(sys.stdin.readline())
conference = list()

for _ in range(N) :
    start,end = map(int,sys.stdin.readline().split(" "))
    conference.append([start,end])

conference.sort(key= lambda x:(x[1],x[0]))
standard = conference[0]
cnt = 1

for s,e in conference[1:] :
    if s < standard[1] :
        continue
    cnt+=1
    standard = [s,e]

print(cnt)