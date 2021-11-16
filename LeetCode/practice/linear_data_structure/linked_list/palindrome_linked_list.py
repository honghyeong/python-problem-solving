#234



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# List

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q:List=[]
        if not head:
            return True
        
        node=head
        #linkedlist convert to list
        while node is not None:
            q.append(node.val)
            node=node.next
        #check palindrome
        
        return q[:]==q[::-1]
        
# Deque 
import collections
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        #declare Deque datatype
        q:Deque=collections.deque()
        if not head:
            return True

        node=head
        #linkedlist convert to list
        while node is not None:
            q.append(node.val)
            node=node.next

        #check palindrome
        while len(q)>1:
            if q.popleft()!=q.pop():
                return False
        return True
    
# Runner     
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        rev=None
        slow=fast=head
        # make rev by Runner
        while fast and fast.next:
            fast=fast.next.next
            rev,rev.next,slow=slow,rev,slow.next
        if fast:
            slow=slow.next

        # check palindrome
        while rev and rev.val == slow.val:
            slow,rev=slow.next,rev.next
        return not rev
