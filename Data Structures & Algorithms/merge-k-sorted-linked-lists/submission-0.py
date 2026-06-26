# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergedLists(l1, l2))
            lists = temp
        
        return lists[0]

    def mergedLists(self, lists1, lists2):
        node = ListNode()
        ans = node
        while lists1 and lists2:
            if lists1.val > lists2.val:
                node.next = lists2
                lists2 = lists2.next
            else:
                node.next = lists1
                lists1 = lists1.next
            node = node.next             
                
        if lists1:
            node.next = lists1
        if lists2:
            node.next = lists2
                

        return ans.next
            

        