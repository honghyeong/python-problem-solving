#332

# Recursive DFS
# 지금까지 dfs 이동하면서 이동자취 기록한 것과 달리
## 한붓그리기같은 탐색을 시도한 문제. 한번의 순회로 끝나는 경로를 찾는다.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=collections.defaultdict(list)
        # 그래프 사전어휘순으로 형성
        for a,b in sorted(tickets):
            graph[a].append(b)

        route=[]

        def dfs(a):
            # 첫번째 값을 읽어 해당 장소 방문
            if graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)             ### 이 부분이 굳이 뒤에 있어야 하는 이유,

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]       
        
        ### 이 부분에서 방문 경로를 뒤집는 이유. 첫 번째 방문에서 모든 경로를 들를 수 도 있다.
        ### 하지만 dfs 재귀탐색이 종료 된 후, 확실하게 모든 노드를 방문한 route값이 나오고, 그 경로는 dfs에서 마지막 탐색값부터 거꾸로 추가된 값이므로 역순으로 취해준다.
        
## graph 사전순 방문에서 pop(0) : O(n)을 pop(): O(1)로 변경.        
        
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=collections.defaultdict(list)

        for a,b in sorted(tickets,reverse=True):
            graph[a].append(b)

        route=[]

        def dfs(a):
            # 첫번째 값을 읽어 해당 장소 방문
            if graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')

        return route[::-1]
        
## Stack Itertaion Solution

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=collections.defaultdict(list)
        # 그래프 사전어휘순으로 형성
        for a,b in sorted(tickets):
            graph[a].append(b)

        route=[]
        stack=['JFK']
        
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop()) ## 그래프의 경로 끊김을 풀어내주는 역할

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
