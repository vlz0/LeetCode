"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr=Node(-1)
        curr=head
        while curr: #Copy List
            ptr.next=Node(-1)
            temp=curr.next
            ptr.next.val=curr.val
            curr.next=ptr.next
            ptr.next.next=temp
            curr=temp
        curr=head
        while curr: #Set Random Pointers
            if curr.random==None:
                curr.next.random=None
            else:
                temp=curr.random
                curr.next.random=temp.next
            curr=curr.next.next
        curr=head
        dp=ptr=Node(-1)
        while curr: #Demerging the copy list and original list
            temp=curr.next.next
            ptr.next=curr.next
            curr.next=temp
            curr=temp
            ptr=ptr.next
        return dp.next
