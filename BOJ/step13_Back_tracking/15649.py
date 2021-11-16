from typing import *

# prev_elements의 append, pop을 이용한 backtracking

def dfs(elements:List[int],M:int): # 재귀 backtracking을 구현할 dfs

    if M==0:   # M 횟수만큼 elements 추가, 다 추가했으면, 종료
        result.append(prev_elements[:])  # 결과에 생성된 배열 추가
        return

    for e in elements:
        next_elements = elements.copy()   # 추가한 원소를 뺀, 배열을 생성하여 다음 dfs에 전달
        next_elements.remove(e)

        prev_elements.append(e)     # 원소 추가

        dfs(next_elements,M-1)      # 재귀
        prev_elements.pop()     # 결과에 추가했으면, leef node에서 올라오면서 pop




N,M=map(int,input().split())
arr=list(range(1,N+1))

result=[]
prev_elements=[]

dfs(arr,M)

for i in result: # 
    for x in i:
        print(x,end=' ')
    print('')


# path=[] 를 parameter로 활용했을 때 dfs
from typing import *
N,M=map(int,input().split())

result=[]

elements=[ x for x in range(1,N+1)]

prev_result=[]

def dfs(a_elements,path:List=[]):
    if len(path)==M:
        result.append(path)
        return

    for i in a_elements:

        next_elements=a_elements.copy()
        next_elements.remove(i)
        dfs(next_elements,path+[i])


dfs(elements,[])
print(result)
