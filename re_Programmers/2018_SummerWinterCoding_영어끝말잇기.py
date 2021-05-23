'''
n	words	result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]
'''


def solution(n, words):
    used = [words[0]]
    idx = 0

    for nowWord,nextWord in zip(words,words[1:]) :
        idx += 1
        if nowWord[-1] != nextWord[0] or nextWord in used or len(nextWord) == 1 :
            return [idx%n+1,idx//n+1]
        used.append(nextWord)

    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))