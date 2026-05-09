# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left_ = max(0, dfs(node.left))
            right_ = max(0, dfs(node.right))

            res = max(left_ + right_ + node.val, res)

            return max(left_, right_) + node.val
        dfs(root)
        return res
