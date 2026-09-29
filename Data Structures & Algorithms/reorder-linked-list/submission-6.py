class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Trouver le milieu
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Inverser la deuxième moitié
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev

        # 3. Fusionner les deux moitiés
        first = head

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second