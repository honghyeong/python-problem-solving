N,M=map(int,input().split())

def gcf(N:int,M:int)->int:
    start=min(N,M)
    for i in range(start,0,-1):
        if N%i==0 and M%i==0:
            return i

def lcm(N:int,M:int)->int:
    start=value=max(N,M)
    while True:
        if start%N==0 and start%M==0:
            return start
        start+=value

print(gcf(N, M))
print(lcm(N,M))
