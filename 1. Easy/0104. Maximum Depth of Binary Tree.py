# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxSum, stack = 1, [[root, 1]]
        while stack:
            currentNode, currentSum = stack.pop()
            if currentNode is None: continue
            stack.append([currentNode.left,currentSum+1])
            stack.append([currentNode.right,currentSum+1])
            maxSum = max(maxSum,currentSum)
        return maxSum if root is not None else 0
