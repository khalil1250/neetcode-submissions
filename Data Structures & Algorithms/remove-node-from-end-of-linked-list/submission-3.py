# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        queue = deque()
        tmp = head
        while tmp is not None:
            queue.append(tmp)
            if len(queue)>n+1:
                queue.popleft()
            tmp = tmp.next

        prev = queue.popleft()
        if prev is head and len(queue) == n-1:
            return head.next
        prev.next = prev.next.next
        return head
        
        

        