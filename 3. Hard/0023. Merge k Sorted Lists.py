# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lista = []
        for i in lists:
            temporal = i
            while temporal:
                lista += [temporal.val]
                temporal = temporal.next
        lista = sorted(lista, reverse = True)
        respuesta = None
        for i in lista:
            respuesta = ListNode(i, respuesta)
        return respuesta
