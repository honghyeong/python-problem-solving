# Knap Sack algorithm
# Out of Memory  : Maybe 2D array.
N,C=map(int,input().split())
weight=list(map(int,input().split()))

weight.sort()

P=[[0 for x in range(C+1)] for x in range(N+1)]

for n in range(N+1):
    for w in range(C+1):
        if n==0 or w==0:
            P[n][w]=1
        elif weight[n-1]<=w:
            P[n][w]=P[n-1][w-weight[n-1]]+P[n-1][w]
        else:
            P[n][w]=P[n-1][w]
print(P[N][C])

# Knap Sack Algorithm 2
# 1D array.
