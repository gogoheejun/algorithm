# import sys
# sys.stdin = open("input.txt", "r")
# n = int(input())
# for i in range(1, n+1):
#     str = input()
#     str = str.upper()
#     for j in range(len(str)//2):
#         if str[j] != str[-1-j]:
#             print("#%d NO" % i)
#             break
#     else:
#         print("#%d YES" % i)

# 파이썬 거꾸로 리스트표시해도 됨
import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
for i in range(n):
    str = input()
    str = str.upper()
    if str == str[::-1]:
        print("#%d YES" % i)
    else:
        print("#%d NO" % i)

# a = [1, 2, 3, 4, 5]
# b = a[::-1]
# print(b)
