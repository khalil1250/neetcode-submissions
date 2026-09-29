# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        last = head
        replica = None
        l = 0
        while last is not None:
            replica = ListNode(last.val, replica)
            print(last.val, replica.next)
            last = last.next
            l+=1

        temp = head
        toRep = True
        res = head.next
        print(l)
        i = 1
        while i != l:
            print(i)
            if toRep:
                temp.next = replica
                replica = replica.next
                temp = temp.next
            else:
                temp.next = res
                res = res.next
                temp = temp.next
            toRep = not toRep
            i+=1
        temp.next = None
                