import collections
from typing import *
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=collections.defaultdict(list)

        for u,v,w in times: # 그래프 인접리스트 생성 (출발점, 도착점, 비용)
            graph[u].append((v,w))

        Q=[(0,k)] # 우선순위 큐 생성, (출발점으로부터 비용, 정점의 이름) , 따라서 출발점은 (0,K)

        dist=collections.defaultdict(int) # { 정점의 이름 : 출발점으로부터 비용 }

        while Q:
            time,node=heapq.heappop(Q)
            if node not in dist:
                dist[node]=time
                for v,w in graph[node]:
                    alt=time+w
                    heapq.heappush(Q,(alt,v))

        if len(dist)==n:
            # 전체 노드 개수만큼이 모두 dist에 있다면, 모든 노드의 최단 경로를 구했다는 의미이고, 이는 모두 시작점에서 도달이 가능하다는 의미이다.
            # 만약 노드 개수가 하나라도 모자란다면 그 노드는 시작점에서 도달할 수 없다는 뜻.
            return max(dist.values())
        return -1
