'''
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
'''

import re
def solution(files):
    d = dict()
    for i in files :
        init = []
        answer = re.findall('\D+|\d+',i)
        init.append(answer[0].lower())
        init.append(int(answer[1]))
        d[i] = init
    d = sorted(d.items(), key=lambda x:(x[1][0],x[1][1]))
    answer = []

    for i in d :
        answer.append(i[0])

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))