import sys
sys.stdin = open("input.txt", "r")


def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+T[L] <= n+1:
            DFS(L+T[L], sum+P[L])
        # 상담 안받는날은 그냥 1씩증가
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)  # 하나씩 밀리게 함.1일에 인덱스1이 되게
    P.insert(0, 0)
    DFS(1, 0)
    print(res)
