from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1 : return False
        openToClose = {
            '(':')', '[':']', '{':'}'
        }
        queue = deque()

        for ch in s:
            if ch in openToClose.keys():
                queue.append(ch)
            else:
                if len(queue) == 0 : return False
                match = queue.pop()
                if openToClose[match] != ch:
                    return False
        if len(queue) != 0 : return False
        return True
        
        