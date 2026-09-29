# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        curr1 = list1 
        curr2 = list2
        tmp = None
        if curr1.val<= curr2.val:
                tmp = curr1
                curr1 = curr1.next
        else : 
            tmp  = curr2
            curr2 = curr2.next
        res = tmp
        while(curr1 is not None and curr2 is not None):
            if curr1.val<= curr2.val:
                tmp.next = curr1
                curr1 = curr1.next
                tmp = tmp.next
            else : 
                tmp.next = curr2
                curr2 = curr2.next
                tmp = tmp.next
        
        if curr1 is None:
            tmp.next = curr2
        else: tmp.next = curr1

        return res

            
        