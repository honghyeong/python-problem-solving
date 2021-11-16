import sys
# input
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

arr.sort()
min_value=sys.maxsize
# two pointer
left,right=0,n-1
while left<right:
    if arr[left]+arr[right]>0:
        if abs(arr[left]+arr[right])<min_value: # check whether min_value or not
            min_value=abs(arr[left]+arr[right])
            result=[arr[left],arr[right]]
        right-=1

    elif arr[left]+arr[right]<0:
        if abs(arr[left]+arr[right])<min_value:  # check whether min_value or not
            min_value=abs(arr[left]+arr[right])
            result=[arr[left],arr[right]]
        left+=1
    else:
        result=[arr[left],arr[right]]
        min_value=0
        left+=1 # Find another answer 
        right-=1 # Find another answer

for i in result:
    sys.stdout.write(str(i)+' ')
