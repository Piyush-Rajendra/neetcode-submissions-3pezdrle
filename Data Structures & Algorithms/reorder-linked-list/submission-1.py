# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # Find the middle of the list using slow/fast pointers
        # slow moves 1 step, fast moves 2 steps
        # when fast reaches the end, slow is at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        second = slow.next  # second half starts from the node after middle
        prev = slow.next = None  # cut the list (slow.next = None) and initialize prev for reversal
        
        # Reverse the second half of the list
        while second:
            tmp = second.next  # save the next node before we lose it
            second.next = prev  # reverse: make current node point backwards to prev
            prev = second  # move prev forward to current node (it's now part of reversed portion)
            second = tmp  # move to the next node (using saved tmp)
        # After loop: prev points to the head of the reversed second half
        
        # Merge the two halves by alternating nodes
        first, second = head, prev  # first half starts at head, second half starts at prev (reversed)
        while second:  # continue while second half has nodes (it's shorter or equal length)
            temp1, temp2 = first.next, second.next  # save next nodes from both halves
            first.next = second  # link first node to second node (weaving)
            second.next = temp1  # link second node back to the next first node
            first, second = temp1, temp2  # advance both pointers to next pair


              

        

        