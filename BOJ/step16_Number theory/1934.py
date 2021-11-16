import sys
def lcm(N:int,M:int)->int:
    start=value=max(N,M)
    while True:
        if start%N==0 and start%M==0:
            return start
        start+=value
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    print(lcm(A, B))
