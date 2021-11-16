# Top-down Dynamic programming : Memoization
import collections
dp=collections.defaultdict(int)
dp[-1]=1
dp[0]=0
dp[1]=1
def fiboacci(n:int):
    if n==0:
        return dp[0]
    if n==1:
        return dp[1]
    if dp[n]:
        return dp[n]
    dp[n]=fiboacci(n-1)+fiboacci(n-2)
    return dp[n]

T=int(input())

for i in range(T):
    n=int(input())
    fiboacci(n)
    print(dp[n-1],dp[n],sep=' ')

    
# Bottom-up Dynamic Programming : Tablulation    
T=int(input())
for i in range(T):
    n=int(input())
    one=0
    zero=1
    for _ in range(n):
        zero,one=one,one+zero
    print(zero,one)
