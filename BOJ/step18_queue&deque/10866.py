import sys
from typing import *
import collections

input=sys.stdin.readline

N=int(input())
deq=collections.deque()

for _ in range(N):
    a=list(input().split())

    if a[0]=='push_front':
        deq.appendleft(int(a[1]))
    elif a[0]=='push_back':
        deq.append(int(a[1]))
    elif a[0]=='pop_front':
        if len(deq):
            print(deq.popleft())
        else:
            print(-1)
    elif a[0]=='pop_back':
        if len(deq):
            print(deq.pop())
        else:
            print(-1)
    elif a[0]=='size':
        print(len(deq))
    elif a[0]=='empty':
        if len(deq):
            print(0)
        else:
            print(1)
    elif a[0]=='front':
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    elif a[0]=='back':
        if len(deq):
            print(deq[-1])
        else:
            print(-1)
