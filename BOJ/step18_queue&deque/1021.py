import collections
from typing import*


def circular_queue(arr: List, N: int) -> int:
    deque: Deque = collections.deque(list(range(1, N + 1)))
    result = 0
    for i in arr:
        if abs(deque.index(i)) < abs(len(deque)- deque.index(i)): # 최소로 이동하기위한 방향 결정
            while deque[0] != i:
                deque.append(deque.popleft())
                result += 1
            deque.popleft()
        else:
            while deque[0] != i:
                deque.appendleft(deque.pop())
                result += 1
            deque.popleft()
    return result


N,M=map(int,input().split())
arr=list(map(int,input().split()))
print(circular_queue(arr,N))
