# 787

import collections
from typing import *
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        # 그래프 인접 리스트 구성
        graph=collections.defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))

        # 큐 변수 : (비용,정점,남은 가능 경유지 수)
        Q=[(0,src,K)]

        while Q:
            price,node,k=heapq.heappop(Q)
            if node==dst:
                return price
            if k>=0: # K=0일때, 한번 이동하는 것으로 치는 문제이기 때문
                for v,w in graph[node]:
                    alt=price+w
                    heapq.heappush(Q,(alt,v,k-1))
                    
        return -1
