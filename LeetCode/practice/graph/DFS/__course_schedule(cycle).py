#207
# Check whether cycle graph or not

# Recursive 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=collections.defaultdict(list)

        for x,y in prerequisites:
            graph[x].append(y)

        traced=set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


# Optimization by pruning
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=collections.defaultdict(list)

        for x,y in prerequisites:
            graph[x].append(y)

        traced=set()
        visited=set()

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            return True

        for x in list(graph):  ####### python 공식 인터프리터인  C Python의 원리와 특징
            if not dfs(x):
                return False

        return True

