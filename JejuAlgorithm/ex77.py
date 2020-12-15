# 1. LCS(Longest Common Subsequence) 알고리즘이란?
#   : 최장 공통 부분 문자열

# 가장 긴 공통 부분 문자열이란 A,B 두 문자열이 주어졌을 때 두 열에 공통으로 들어 있는 요소로 만들 수 있는 가장 긴 부분열을 말합니다.
# 여기서 부분열이란 다른 문자열에서 몇몇의 문자가 빠져 있어도 순서가 바뀌지  않은 열을 말합니다.
# 예를 들어 S1 = [’T’,’H’,’E’,’S’,’T’,’R’,’I’,’N’,’G’,’S’]
# 	      S2 = [’T’,’H’,’I’,’S’,’I’,’S’]
# 라는 두 문자열이 있을 때 둘 사이의 부분 공통 문자열의 길이는
# [’T’,’H’,’S’,’T’,’I’,’S’] 6개가 됩니다.
#
# 이처럼 두 문자열이 주어지면 가장 긴 부분 공통 문자열의 길이를 반환하는 프로그램을 만들어 주세요.
#
# 두 개의 문자열이 한 줄에 하나씩 주어집니다.
# 문자열은 알파벳 대문자로만 구성되며 그 길이는 100글자가 넘어가지 않습니다.
#
# 출력은 이 두 문자열의 가장 긴 부분 공통 문자열의 길이를 반환하면 됩니다.
# ------------------------------------------------------------------------------------------------------------------
# LCS(Longest Common Subsequence) 알고리즘 구현 과정
# 1.  X = (x1, x2...xn), Y = (y1, y2...yn)
# 2.  LCS(Xi,Yj) = 0                                     ( if i=0 or j=0 )
#                = LCS(X(i-1),Y(i-1)) +1                 ( if Xi = Yj )
#                = max( LCS(Xi,Y(j-1) , LCS(X(i-1),Yj) ) ( if Xi ≠ Yj )