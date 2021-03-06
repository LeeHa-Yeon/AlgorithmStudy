# 문제 81 : 지뢰찾기
#
# 지뢰를 찾는 문제입니다. 다음 그림처럼 깃발 주위에는 지뢰가 사방으로 있습니다.
# 깃발의 위치를 입력받아 지뢰와 함께 출력해주는 프로그램을 만드세요.
#
# 아래 case 외 예외 사항은 고려하지 않습니다.
# (예를 들어 깃발이 붙어 있을 경우는 고려하지 않습니다)
# 실력이 되시는 분들은 깃발이 붙어있을 상황까지 고려해주세요

# 입력
# 0 1 0 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 0 0 1 0 0
# 0 0 0 0 0

# 출력
# * f * 0 0
# 0 * 0 * 0
# 0 0 * f *
# 0 * f * 0
# 0 0 * 0 0

minesweeper = '0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0'
minesweeper = minesweeper.replace('1','f')
minesweeper = minesweeper.split(' ')


for i in range(len(minesweeper)) :

    if minesweeper[i] == 'f' :
        if i % 5 > 0 :
            minesweeper[i-1] = '^'
        if (i+1) % 5 > 0 :
            minesweeper[i+1] = '$'
        if i > 4 :
            minesweeper[i - 5] = '#'
        if i < 20 :
            minesweeper[i + 5] = '*'

for i in range(len(minesweeper)) :
    if i%5==0 and i!=0:
        print()
    print(minesweeper[i],end='')