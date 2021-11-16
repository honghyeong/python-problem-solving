#3273
import sys
# input
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline())

result=0
arr.sort()
# two pointer
left,right=0,n-1
while left<right:
    if arr[left]+arr[right]<x:
        left+=1
    elif arr[left]+arr[right]>x:
        right-=1
    else:
        result+=1
        left+=1 # Find another answer
        right-=1 # Find another answer
print(result)

