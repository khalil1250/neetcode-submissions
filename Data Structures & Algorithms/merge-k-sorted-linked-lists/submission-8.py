import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = [
            (node.val, i)
            for i, node in enumerate(lists)
            if node is not None
        ]

        heapq.heapify(heap)

        dummy = ListNode()
        tail = dummy

        while heap:
            _, i = heapq.heappop(heap)

            node = lists[i]
            lists[i] = node.next

            tail.next = node
            tail = node

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next