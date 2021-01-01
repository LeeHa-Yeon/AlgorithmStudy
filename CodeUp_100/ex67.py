#   12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

num = int(input())

if 3<= num <= 5 :
    print("spring")
elif 6<= num <= 8 :
    print("summer")
elif 9<= num <= 11 :
    print("fall")
else :
    print("winter")


# month = int(input())
# if month in (12, 1, 2):
#     print('winter')
# elif month in (3,4,5):
#     print('spring')
# elif month in (6,7,8):
#     print('summer')
# else:
#     print('fall')