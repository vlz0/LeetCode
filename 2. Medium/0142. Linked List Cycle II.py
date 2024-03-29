# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, root: Optional[ListNode]) -> Optional[ListNode]:
        n = 1000000
        while(root!= None and root.val != 1000000):
            root.val = 1000000
            root = root.next
        return root
