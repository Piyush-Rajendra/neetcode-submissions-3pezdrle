# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # store values of inorder in hashmap for constant time lookup
        indices = {val:idx for idx, val in enumerate (inorder)}
        #declare variable to store index of preorder
        self.idx_pre = 0
        def dfs(l, r):

            if l > r:
                return None
            #store value of preorder to construct tree
            root_val = preorder[self.idx_pre]
            #increment preorder index to traverse 
            self.idx_pre += 1
            #construct root
            root = TreeNode(root_val)
            #binary search, find value of mid from hashmap 
            mid = indices[root_val]
            #get left and right nodes for root and return root
            root.left = dfs(l, mid -1)
            root.right = dfs(mid + 1, r)
            return root
        #run dfs using inorder lengths as r and l as 0
        return dfs(0, len(inorder) - 1 )
            
        