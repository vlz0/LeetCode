# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        while q:
            lis = []
            for i in range(len(q)):
                ele = q.popleft()
                if ele:
                    lis.append(ele.val)
                    q.append(ele.left)
                    q.append(ele.right)
            if lis:
                res.append(lis)
        return res[::-1]
