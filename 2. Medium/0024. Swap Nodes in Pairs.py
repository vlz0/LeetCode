# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cabeza = head
        while cabeza and cabeza.next:
              cabeza.val, cabeza.next.val = cabeza.next.val, cabeza.val
              cabeza = cabeza.next.next
        return head
