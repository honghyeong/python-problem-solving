# 406
# why? greedy algorithm?
# local optimal greedy choice = 키 큰 사람부터 세우는 것.
# 크거나 같은 사람들이 앞에 채워졌으므로 index에 따라 위치 정리.

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap=[]
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap,(-person[0],person[1]))

        result=[]
        # 키 역순, 인덱스 추출
        while heap:
            person=heapq.heappop(heap)
            result.insert(person[1],[-person[0],person[1]])

        return result
    
