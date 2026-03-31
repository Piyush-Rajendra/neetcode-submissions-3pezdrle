# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return
        
        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split and reverse second half
        second = slow.next
        slow.next = None
        second = self.reverse(second)
        
        # Step 3: Merge
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
    
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        
        return prev


              

        

        