# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        i = 1
        while i < left:
            prev = curr
            curr = curr.next
            i += 1
        groupStart = curr

        j = left
        while j < right:
            prev_r = curr
            curr = curr.next
            j += 1
        
        groupEnd = curr

        temp = groupEnd.next
        prev_r = None
        curr = groupStart
        while curr != temp:
            tmp = curr.next
            curr.next = prev_r
            prev_r = curr
            curr = tmp
        
        prev.next = groupEnd
        groupStart.next = temp

        return dummy.next

