# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while any(lists):
            val, idx = min((li.val, idx) for idx, li in enumerate(lists) if li)
            curr.next = ListNode(val)
            curr = curr.next
            lists[idx] = lists[idx].next
        return dummy.next