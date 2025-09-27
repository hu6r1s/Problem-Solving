# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     dummy = curr = ListNode()
    #     while any(lists):
    #         val, idx = min((li.val, idx) for idx, li in enumerate(lists) if li)
    #         curr.next = ListNode(val)
    #         curr = curr.next
    #         lists[idx] = lists[idx].next
    #     return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(li.val, idx) for idx, li in enumerate(lists) if li]
        heapq.heapify(heap)

        dummy = curr = ListNode()
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        return dummy.next