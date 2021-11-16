# Excess time limit - my solution

import heapq
import sys
heap=[]
input=sys.stdin.readline
N=int(input())
temp=[]

for i in range(N):
    a=int(input().strip())
    heapq.heappush(heap,a)
    if i%2==0: # 홀수개 삽입
        for _ in range((i+2)//2):
            temp.append(heapq.heappop(heap))
    else: # 짝수개 삽입
        for _ in range((i+1)//2):
            temp.append(heapq.heappop(heap))
    # print('temp', temp)
    print(temp[-1])

    while temp:
        heapq.heappush(heap,temp.pop())
    # print('heap',heap)

