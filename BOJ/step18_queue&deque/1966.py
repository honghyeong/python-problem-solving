import sys
from typing import *
import collections
def print_queue(arr):

    queue:Deque=collections.deque(arr)

    count=0
    while queue:
        if max(queue)==queue[0]:
            if type(queue.popleft())==float:
                return count+1
            count+=1
        else:
            queue.append(queue.popleft())

input=sys.stdin.readline

N=int(input())
for _ in range(N):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))

    arr[M]=float(arr[M]) # hang a mark ( type float)

    print(print_queue(arr))
