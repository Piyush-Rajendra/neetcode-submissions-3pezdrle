# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            
            include_left, exclude_left = dfs(node.left)
            include_right, exclude_right = dfs(node.right)

            include_current = node.val + exclude_left + exclude_right
            exclude_current = max(include_left , exclude_left) + max(include_right , exclude_right)

            return(include_current, exclude_current)

        include, exclude = dfs(root)

        return max(include, exclude)
        