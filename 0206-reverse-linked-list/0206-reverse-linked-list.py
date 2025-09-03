# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        dummy = ListNode()
        output = dummy
        while stack:
            output.next = stack.pop()
            output = output.next

        output.next = None
        return dummy.next
