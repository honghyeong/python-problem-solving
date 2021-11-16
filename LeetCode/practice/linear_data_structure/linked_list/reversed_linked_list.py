#206 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive reverse linkedlist
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node:ListNode,prev:ListNode=None):
            if not node:
                return prev
            next_node,node.next=node.next,prev
            
            return reverse(next_node,node)
        return reverse(head)
        
 # Iterative reverse linkedlist
 class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node,prev=head,None

        while node:
            node.next,nextnode=prev,node.next
            prev,node=node,nextnode
            
        return prev
