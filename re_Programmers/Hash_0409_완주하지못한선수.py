'''
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
'''

def solution(participant, completion):

    participant.sort()
    completion.sort()
    answer = ""

    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
        answer = participant[i+1]
    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))