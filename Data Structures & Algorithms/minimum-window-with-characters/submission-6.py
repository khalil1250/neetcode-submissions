from collections import defaultdict
class Solution:

    def tSeen(self, seen, tt):
        for k in tt:
            if(seen[k]<tt[k]):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        seen = defaultdict(int)
        tt = defaultdict(int)
        for c in t:
            tt[c] += 1
        left = 0
        right = 0
        while right < len(s) and not self.tSeen(seen, tt):
            seen[s[right]] += 1
            right+=1
        if self.tSeen(seen, tt):
            while(seen[s[left]] -1 >= tt[s[left]] ):
                seen[s[left]] -= 1
                left+=1
            res = s[left:right]
        else: return res
        
        for r in range(right, len(s)):
            seen[s[r]] += 1
            if s[r] in tt:
                while(seen[s[left]] -1 >= tt[s[left]] ):
                    seen[s[left]] -= 1
                    left+=1
                if r-left+1 < len(res):
                    res = s[left:r+1]
        return res
