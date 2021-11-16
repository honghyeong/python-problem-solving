import heapq
import sys
heap=[]
input=sys.stdin.readline
N=int(input())

for _ in range(N):
    a=int(input().strip())

    if a!=0:
        heapq.heappush(heap,(abs(a),a)) # abs값으로 먼저 우선순위 비교, 그 다음 a값으로 우선순위 비교
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
