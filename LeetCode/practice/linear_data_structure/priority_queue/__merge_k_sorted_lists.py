#23


# Use Minheap : import heapq
# Priority Queue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root=result=ListNode(None)
        heap=[]

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
            
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node=heapq.heappop(heap)
            idx=node[1]
            result.next=node[2]
            
            result=result.next
            if result.next: # heappop으로 각 연결리스트의 루트 노드가 나왔고, 그 다음 노드도 딸려나왔으므로, 다음 노드가 존재한다면
                heapq.heappush(heap,(result.next.val,idx,result.next)) # 그 다음노드부터 다시 heap에 idx를 유지해서 넣어준다.

        return root.next
