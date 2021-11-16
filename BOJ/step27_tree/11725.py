import collections
import copy

N=int(input())
graph=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

stack=[1]
who_is_parent=collections.defaultdict(list)

while stack:
    node=stack.pop() # stack dfs

    for w in graph[node]:
        who_is_parent[w].append(node)
        stack.append(w)
        graph[w].remove(node) # 그래프 간 간선이 양방향이므로, 이렇게되면 다시 부모노드로 돌아가는 무한 루프가 생기므로, 자식에서 부모노드로 가는 노드는 제거.

for i in range(2,N+1):
    print(who_is_parent[i][0])
