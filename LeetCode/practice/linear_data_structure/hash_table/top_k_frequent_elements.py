#347

# Use Counter, MaxHeap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs=collections.Counter(nums)
        freqs_heap=[]
        
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heaeppush(freqs_heap,(-freqs[f],f))
        
        topk=list()
        # k번 만큼 추출
        
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            
        return topk

# Pythonic way  
import collections
from typing import *
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
