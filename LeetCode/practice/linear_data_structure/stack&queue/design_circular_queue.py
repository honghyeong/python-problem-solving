#622
class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[None]*k
        self.maxlen=k
        self.p1=0 # front pointer
        self.p2=0 # rear pointer

    def enQueue(self, value: int) -> bool: #move rear pointer
        if self.q[self.p2] is None:
            self.q[self.p2]=value
            self.p2=(self.p2+1)%self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None: # move front pointer
            return False
        else:
            self.q[self.p1]=None
            self.p1=(self.p1+1)%self.maxlen
            return True


    def Front(self) -> int:
        if self.q[self.p1] is None:
            return -1
        else:
            return self.q[self.p1]

    def Rear(self) -> int: # rear pointer는 이미 추가할 자리를 위해 이동한 상태이므로 그 전 위치를 반환
        if self.q[self.p2-1] is None:
            return -1
        else:
            return self.q[self.p2-1]

    def isEmpty(self) -> bool:
        return self.p1==self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1==self.p2 and self.q[self.p1] is not None
