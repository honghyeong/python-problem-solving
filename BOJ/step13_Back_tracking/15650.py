
N,M=map(int,input().split())

result=[]
prev_elements=[]

def dfs(start,M):

    if M==0:
        result.append(prev_elements[:])

    for i in range(start,N+1):
        prev_elements.append(i)
        dfs(i+1,M-1)
        prev_elements.pop()

dfs(1,M)

for i in result:
    for elements in i:
        print(elements,end=' ')
    print('')
