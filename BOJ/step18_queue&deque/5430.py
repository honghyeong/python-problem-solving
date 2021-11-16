import sys
import collections
input=sys.stdin.readline

N=int(input())

for _ in range(N):
    opeartion=input().strip()
    num=int(input())
    temp = input().strip().replace('[','')
    temp = temp.replace(']', '')
    if temp == '':
        arr=[]
    else:
        arr = list(map(int, temp.split(',')))

    deq = collections.deque(arr)
    flag=True
    R=1
    for i in opeartion:
        if i=='R':
            R+=1
        elif i=='D':
            if len(deq):
                if R%2==1: # 일일이 deq.reverse()하지않고, R개수에 따라 제거할 위치 결정
                    deq.popleft()
                else:
                    deq.pop()
            else:
                flag = False
                break
    if R%2==0:
        deq.reverse()

    # 제출형식 맞춤.
    
    if flag:
        a=','.join(list(map(str,deq)))
        a='['+a+']'
        print(a)
    else:
        print('error')

