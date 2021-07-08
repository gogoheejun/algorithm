import sys
# sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        lt += 1
        rt = lt+1
        tot = a[lt]
    else:
        lt += 1
        rt = lt + 1
        tot = a[lt]
print(cnt)
