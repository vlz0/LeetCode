
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, i: int) -> ListNode:
        if not head:
            return None
        ultimo = head
        longitud = 1
        while (ultimo.next):
            ultimo = ultimo.next
            longitud += 1

        i = i % longitud
        ultimo.next = head
        temporal = head

        for _ in range( longitud - i - 1 ):
            temporal = temporal.next
        
        final = temporal.next
        temporal.next = None
        
        return final
