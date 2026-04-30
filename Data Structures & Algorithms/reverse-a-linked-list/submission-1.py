# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            # change the direction of pointers
            # 1-> 2 : 1 <- 2
            # so we are doing 
            '''
            storing value of current.next(2) in temp
            then reverse current.next with current(1)
            and then put temp(2) in curr
            so but in linked list we need to take of connected nodes so we use Prev pointer and curr pointer to maintain
            the nodes
            '''
            nextNode = current.next #store curr.next so that we know where to point
            current.next = previous
            previous = current
            current = nextNode

        return previous
        