from collections import deque

def solution(begin, target, words):
    words = words
    queue = deque([begin])
    diff =[]
    answer = 0
    if target not in words:
        return 0

    while queue:
        current = queue.popleft()
        for word in words:
            cnt = 0
            for i in range(len(word)):
                if current[i] != word[i]:
                    cnt += 1
            if cnt >= 2:
                diff.append(word)
                continue
            elif cnt == 1:
                if word == target:
                    answer += 1
                    return answer
                else:
                    queue.append(word)
        words = words[len(queue):] + diff
        if queue :
            begin = queue.pop()
            queue = deque([begin])
            answer+=1
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","hhh",["hhh","hht"]))
print(solution("hit","cog",["cog","log","lot","dog","dot","hot"]))


