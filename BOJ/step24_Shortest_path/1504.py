import heapq
import sys
import collections

input=sys.stdin.readline
N,E=map(int,input().split())
graph = collections.defaultdict(list)
INF=sys.maxsize
# 그래프 인접리스트 생성
for _ in range(E):
    a=list(map(int,input().split()))
    graph[a[0]].append((a[1],a[2]))
    graph[a[1]].append((a[0],a[2]))

V1,V2=map(int,input().split())

# 도달할 수 없는 경로는 무한대의 거리로 설정해주는 dijkstra 
def dijkstra(start):
   dist=[INF for _ in range(N+1)]
   dist[start]=0
   Q=[(0,start)]

   while Q:
       weight,node=heapq.heappop(Q)
       for v,w in graph[node]:
            alt=weight+w
            if alt<dist[v]:
                dist[v]=alt
                heapq.heappush(Q,(alt,v))
   return dist

one=dijkstra(1)
V1_start=dijkstra(V1)
V2_start=dijkstra(V2)
# 0-> v1 -> v2 -> N 또는 0 -> v2 -> v1 -> N으로 가는 경로 비교
# 만약 도달 할 수 없는 거리로 return 된다면, INF값이 result에 저장
# 따라서, -1 제출
result=min(one[V1]+V1_start[V2]+V2_start[N], one[V2]+V2_start[V1]+V1_start[N])

print(result if result<INF else -1)
