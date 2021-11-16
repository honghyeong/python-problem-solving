
N=int(input())
arr=list(map(int,input().split()))

answer=[-1]*N
stack=[]
for i,cur in enumerate(arr):
    while stack and cur>arr[stack[-1]]:
        idx=stack.pop()
        answer[idx]=cur
    stack.append(i)

for i in answer:
    print(i,end=' ')
