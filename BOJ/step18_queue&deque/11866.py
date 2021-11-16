import sys
from typing import *
import collections

input=sys.stdin.readline

N,K=map(int,input().split())
arr:Deque=collections.deque(list(range(1,N+1)))

count=0
stack=[]
# 제외될 것은 제거되고, 나머지는 뒤에 이어붙인다는 생각.
# 따라서 제외되지 않은 숫자들은 다시 뒤에 이어붙여줌.
while len(arr)>0:
    count+=1
    if count%K!=0:
        arr.append(arr.popleft())
    else:
        stack.append(arr.popleft())


print('<',end='')
for i in stack[:-1]:
    print(i,end=', ')
print(f'{stack[-1]}>')
