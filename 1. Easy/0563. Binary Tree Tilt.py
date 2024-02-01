# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sumTilt = 0
        def dfs_tilt(root):
            nonlocal sumTilt
            if root is None:
                return
            sumTilt += abs(tree_sum(root.left) - tree_sum(root.right))

            dfs_tilt(root.left)
            dfs_tilt(root.right)

        def tree_sum(root):
            if root is None:
                return 0
            else:
                return root.val + tree_sum(root.right) + tree_sum(root.left)
        dfs_tilt(root)

        return sumTilt
