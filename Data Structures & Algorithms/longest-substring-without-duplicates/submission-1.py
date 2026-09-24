class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        left = 0
        right = 1
        res = 1
        while(right<len(s)):
            while((right<len(s) and s[right] not in s[left:right]) or left==right):
                right += 1
            res = max(right-left, res)
            while((right<len(s) and s[right] in s[left:right]) and left<right):
                left +=1
        return res