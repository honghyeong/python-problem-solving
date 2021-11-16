

import heapq
import sys
heap=[]
input=sys.stdin.readline
N=int(input())
for _ in range(N):
    a=int(input().strip())
    if a>0:
        heapq.heappush(heap,(-a,a)) # how to use maxheap using heapq module
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
