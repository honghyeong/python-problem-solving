# O(n^2) : Brute Force Algorithm

import sys
# input
n,s=map(int,(sys.stdin.readline().split()))
arr=list(map(int,sys.stdin.readline().split()))

result=sys.maxsize
# two pointer
for i in range(n):
    left=i
    length=0
    while left+length!=n:
        if(sum(arr[left:left+length])>s and length <result):
            result=min(result,length)
        length+=1
print(result)


# O(nlogn) or O(n) : Two Pointer Algorithm

import sys
# input
n,s=map(int,(sys.stdin.readline().split()))
arr=list(map(int,sys.stdin.readline().split()))

result=100000
sum_arr=[0] # important part
sum=0
for i in range(n):
    sum_arr.append(sum+arr[i])
    sum+=arr[i]
# two pointer
left=0
right=1
while left!=n:
    if sum_arr[right]-sum_arr[left] <s:
        if right==n:
            left+=1
        else:
            right+=1
    else:
        result=min(result,right-left)
        left+=1

if result==100000:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(result))


