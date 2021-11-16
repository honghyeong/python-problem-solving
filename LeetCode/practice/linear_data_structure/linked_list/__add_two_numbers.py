#2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.


# Change Data type ( Linked List -> list )

class Solution:

    def reverseList(self,head:ListNode)-> ListNode:
        node,prev=head,None
        while node:
            node.next,next=prev,node.next
            prev,node=node,next
        return prev

    def toList(self,node:ListNode)-> List:
        list:list=[]
        while node:
            list.append(node.val)
            node=node.next
        return list

    def toReversedLinkedList(self,result:list)->ListNode:
        prev:ListNode =None
        for r in result:
            node=ListNode(r)
            node.next=prev
            prev=node
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=self.toList(self.reverseList(l1))
        b=self.toList(self.reverseList(l2))
        resultStr=int(''.join(str(e) for e in a))+int(''.join(str(e)for e in b))
        return self.toReversedLinkedList(str(resultStr))


# Full adder : sum, carryin, carryout


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root=head=ListNode(0) # wooooooooooooow
        carry=0
        while l1 or l2 or carry: # perform sum : perform if there is anything
            sum=0
            # sum of inputs
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next

            carry,val=divmod(sum+carry,10)
            head.next=ListNode(val)
            head=head.next
        return root.next # wooooooooooooow
