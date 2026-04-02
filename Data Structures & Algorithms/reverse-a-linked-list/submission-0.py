# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        next_node = None
        while current:
            # keep track of previous node. 
            # for each node point it backwards to the previous node.
            # move forward.
            next_node = current.next

            current.next = prev

            prev = current
            current = next_node

        head = prev

        return head 
        