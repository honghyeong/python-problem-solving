import collections
graph=collections.defaultdict(list)
V=int(input())
E=int(input())

for _ in range(E):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,discovered=[]):
    discovered.append(v)

    for w in graph[v]:
        if w not in discovered:
            discovered=dfs(w,discovered)

    return discovered

print(len(dfs(1))-1) # start vertext : 1 
