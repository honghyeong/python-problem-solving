N,M=map(int,input().split())

result=[]
prev_elements=[]

def dfs(start,M,path):

    if M==0:
        result.append(path[:])
        return

    for i in range(start,N+1):
        dfs(i,M-1,path+[i])


dfs(1,M,[])

for i in result:
    for elements in i:
        print(elements,end=' ')
    print('')
