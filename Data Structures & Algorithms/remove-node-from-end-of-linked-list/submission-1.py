# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # dummy node before head handles edge cases
        fast = dummy # left starts at dummy
        slow = dummy # right starts at head

        for i in range(n+1): # move right pointer n steps ahead to create gap
            fast = fast.next
        
        # move both pointers together maintaining gap the way
        # when right reaches end left is  at node Before the node the to delete
        while fast:       
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next # skip the nth node from end
        return dummy.next # return head (dummy.next)
        




