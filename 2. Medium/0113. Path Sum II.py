# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        b = []

        def dfs(node,a) :
            if not node :
                return None
            a = a + [node.val]
            if node.left : 
                dfs(node.left,a)
            if node.right :
                dfs(node.right,a)
            if not node.left and not node.right :
                sum=0
                for i in a :
                    sum += i

                if sum == targetSum :
                    b.append(a)
                else :
                    a.pop(-1)
            return b
       
        return dfs(root, [])     
