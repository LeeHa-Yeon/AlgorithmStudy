def solution(participant, completion):
    participant.sort()
    completion.sort()

    n = len(participant)

    for i in range(n-1) :
        if participant[i] != completion[i] :
            return participant[i]

    return participant[n-1]

#print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
#print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))