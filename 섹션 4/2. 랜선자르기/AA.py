import sys
# sys.stdin = open("input.txt", "r")


def count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt


k, n = map(int, input().split())
Line = []

for _ in range(k):
    Line.append(int(input()))

largest = max(Line)
lt = 1
rt = largest
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
