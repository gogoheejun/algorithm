import sys
# sys.stdin = open("input.txt", "r")

# sort함수를 쓰면 nlong(n)임.
# list가 이미 정렬되어있을 때는 n번만에 가능함. 이건 큰차이

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c+a[p1:]
if p2 < m:
    c = c+b[p2:]
print(c)
