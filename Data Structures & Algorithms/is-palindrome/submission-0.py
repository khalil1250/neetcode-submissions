class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([l.lower() for l in s if l.isalnum()])
        for i in range(len(s)//2):
            if(s[i] != s[-i-1]):
                return False
        return True