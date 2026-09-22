from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)
        if(cs == ct):
            return True
        return False
        