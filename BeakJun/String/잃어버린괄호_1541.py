expressions = input()

expressions = expressions.split("-")

for expIdx in range(len(expressions)) :
    expList = map(int,expressions[expIdx].split("+"))
    expressions[expIdx] = sum(expList)

answer = expressions[0]

for num in expressions[1:] :
    answer-=num

print(answer)





