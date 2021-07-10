import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
Music = list(map(int, input().split()))

lt = Music[-1]
rt = sum(Music)


def count(cap):
    cnt = 1
    sum = 0
    for x in Music:
        if sum+x > cap:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
