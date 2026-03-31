# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
        '''
Use DFS with a bottom-up approach.

We recursively check the left and right subtrees first.
Each DFS call returns two things:
1. Whether the subtree is balanced (True/False)
2. The height of that subtree

We need the height because a tree is balanced only if the height
difference between the left and right subtree is at most 1.

So for each node we check:
abs(left_height - right_height) <= 1

If both subtrees are balanced and the height difference is <= 1,
then the current node is balanced.

The height of the current node is:
1 + max(left_height, right_height)

This way we compute the answer starting from the leaves
and move upward toward the root.
        '''