class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """                
        curr, prev, a, b = root, None, None, None        
        while curr:
            if not curr.left:   
				# find the node that is violating the ordering 
                if prev and curr.val < prev.val:					
                    if not a: # find the first node to swap
                        a = prev
                    b = curr                   
                prev = curr
                curr = curr.right                
            else:
                temp = curr.left
                while temp.right and temp.right is not curr:
                    temp = temp.right
                if temp.right is curr:
                    temp.right = None 
                    if prev and curr.val < prev.val:
                        if not a:
                            a = prev
                        b = curr   
                    prev = curr
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left

		# swap bide values
        a.val,b.val = b.val, a.val
