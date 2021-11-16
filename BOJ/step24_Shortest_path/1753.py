import collections
import heapq
import sys

input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input()) # start
edges=[]
for _ in range(E):
    a=list(map(int,input().split()))
    edges.append(a)

#그래프 인접 리스트 생성
graph=collections.defaultdict(list)
for u,v,w in edges:
    graph[u].append((v,w))

dist=collections.defaultdict(int)
Q=[(0,K)]

while Q:
    weight,node=heapq.heappop(Q)
    if node not in dist:
        dist[node]=weight
        for v,w in graph[node]:
            alt=weight+w
            heapq.heappush(Q,(alt,v))

dist=dict(dist)
for i in range(1,V+1):
    try:
        print(dist[i])
    except KeyError:
        print('INF')
