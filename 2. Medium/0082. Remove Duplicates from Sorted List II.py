# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ejemplo = ListNode(None, None)
        ejemplo.next = head
        anterior = ejemplo
        actual = head
        while actual and actual.next:
            if actual.next.val == actual.val:
                while actual.next and actual.next.val == actual.val:
                    actual = actual.next
                actual.next, actual = None, actual.next
                anterior.next = actual
            else:
                anterior = actual
                actual = actual.next
        return ejemplo.next
