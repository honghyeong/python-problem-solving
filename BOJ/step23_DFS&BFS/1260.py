import collections
graph=collections.defaultdict(list)
N,M,V=map(int,input().split())

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph.keys():
    graph[i].sort()

def dfs(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered=dfs(w,discovered)

    return discovered

def bfs(start_v):

    discovered=[start_v]
    queue=collections.deque([start_v])

    while queue:
        v=queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                queue.append(w)
                discovered.append(w)
    return discovered


dfs_discovered=dfs(V)
bfs_discovered=bfs(V)

for i in dfs_discovered:
    print(i,end=' ')
print('')
for i in bfs_discovered:
    print(i,end=' ')
