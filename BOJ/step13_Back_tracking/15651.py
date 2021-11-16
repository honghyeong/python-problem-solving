N,M=map(int,input().split())

result=[]

def dfs(M,path):

    if M==0:
        result.append(path[:])
        return  # 15650 문제와 다르게 if M==0문 다음 for문에서 start 변수가 없으므로, 재귀 종료조건이 불명확, 따라서 return으로 종료

    for i in range(1,N+1):
        dfs(M-1,path+[i])


dfs(M,[])

for i in result:
    for elements in i:
        print(elements,end=' ')
    print('')
