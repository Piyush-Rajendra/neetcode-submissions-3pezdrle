# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # dummy node before head handles edge cases
        left = dummy # left starts at dummy
        right = head # right starts at head

        while n > 0 and right: # move right pointer n steps ahead to create gap
            right = right.next
            n -= 1
        
        # move both pointers together maintaining gap the way
        # when right reaches end left is  at node Before the node the to delete
        while right:       
            left = left.next
            right = right.next
        
        left.next = left.next.next # skip the nth node from end
        return dummy.next # return head (dummy.next)
        




