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
        required = set(i for i in t)
        for c in t:
            tt[c] += 1
        left = 0
        right = 0
        while right < len(s) and len(required) > 0:
            seen[s[right]] += 1
            if s[right] in required and seen[s[right]] >= tt[s[right]]: 
                required.remove(s[right])
            right+=1
        if len(required) == 0:
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
        