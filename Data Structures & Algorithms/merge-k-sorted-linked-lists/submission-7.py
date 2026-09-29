# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = [(lists[k].val, k) for k in range(len(lists)) if lists[k] is not None]
        if len(heap) == 0: return None

        heapq.heapify(heap)
        tmp = heapq.heappop(heap)[1]
        head = lists[tmp]
        lists[tmp] = lists[tmp].next
        if lists[tmp] is not None:
            heapq.heappush(heap, (lists[tmp].val, tmp))
            
        tmp = head
        while len(heap) != 0:
            val, k = heapq.heappop(heap)
            node = lists[k]
            lists[k]=lists[k].next
            tmp.next = node
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, k))
            tmp = tmp.next
        return head
            
        