# import sys
# sys.stdin = open("input.txt", "r")
# l = int(input())
# list = list(map(int, input().split()))
# m = int(input())
# for _ in range(m):
#     max_idx = list.index(max(list))
#     list[max_idx] = max(list)-1
#     min_idx = list.index(min(list))
#     list[min_idx] = min(list)+1
# print(max(list) - min(list))

import sys
# sys.stdin=open("input.txt", "r")
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()

print(a[L-1]-a[0])
