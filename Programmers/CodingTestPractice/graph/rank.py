## 모든 노드를 시작노드로 해서 dfs 탐색을 하고, 시작 노드에서 각 노드에 도달이 가능한 경우를 connect에 저장.
## 즉 connect에 서로 노드가 직, 간접적으로 연결돼있는지 확인하는 defaultdict(set)이 나온다.
## 자기 자신을 제외한 n-1 노드만큼이 연결돼있으면, 순위를 확정할 수 있다.

from typing import *
import collections
def solution(n, results):


    graph=collections.defaultdict(list)
    connect=collections.defaultdict(set)
    answer=0

    def dfs(start):
        stack = [start]
        visit = []

        while stack:
            node = stack.pop()
            for v in graph[node]:
                if v not in visit:
                    connect[v].add(start)
                    connect[start].add(v)
                    stack.append(v)
                    visit.append(v)

    for i in results:
        graph[i[0]].append(i[1])


    for i in range(1,n+1):
        dfs(i)

    for i in connect:
        if len(connect[i])==n-1:
            answer+=1

    return answer
