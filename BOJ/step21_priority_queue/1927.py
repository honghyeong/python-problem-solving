import heapq
import sys
heap=[]
input=sys.stdin.readline
N=int(input())
for _ in range(N):
    a=int(input().strip())
    if a>0:
        heapq.heappush(heap,a)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
