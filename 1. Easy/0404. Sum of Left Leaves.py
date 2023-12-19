# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,direction):
            if not root:
                return 0
            if not root.left and not root.right and direction == "L":
                return root.val
            return dfs(root.left, "L") + dfs(root.right, "R")
        
        return dfs(root,"R")
