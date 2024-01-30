"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maximo = 0
        for i in root.children:
            maximo = max(self.maxDepth(i), maximo)
        return maximo + 1
