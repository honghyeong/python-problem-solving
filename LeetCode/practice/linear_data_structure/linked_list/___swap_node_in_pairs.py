# 24

# just swap value
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node=head
        while node and node.next:
            node.val,node.next.val=node.next.val,node.val
            node=node.next.next
        return head


# Iteration swap
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root=prev=ListNode(None) # head change problem
        prev.next=head

        while head and head.next:
            second=head.next
            head.next=second.next
            second.next=head

            prev.next=second

            prev=prev.next.next
            head=head.next

        return root.next

# Recursive Swap
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p=head.next
            # return swap result 
            head.next=self.swapPairs(p.next)
            p.next=head
            return p
        return head
